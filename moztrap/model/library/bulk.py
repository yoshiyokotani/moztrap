"""
Parser for text format for bulk test case entry.

"""
class ParsingError(Exception):
    pass



class BulkParser(object):
    """
    Parser for text format for bulk test case entry.

    Parses this format::

        Test that I can log in
        When I click the login button
        Then I am logged in

    Instantiate a ``BulkParser`` and call its ``parse`` method::

        parser = BulkParser()
        data = parser.parse(text)

    Returned data will be a list of dictionaries containing test case data,
    and/or possibly an "error" key containing an error message encountered in
    parsing.

    """
    def parse(self, text):
        """Parse given text and return list of data dictionaries."""
        data = []
        state = self.begin

        lines = text.splitlines()
        error = False

        for line in lines:
            line = line.strip()
            if line:
                try:
                    state = state(line.lower(), line, data)
                except ParsingError as e:
                    data = data or [{}]
                    data[-1]["error"] = str(e)
                    error = True
                    break

        if not error and not state.expect_end:
            if not data:
                data.append({})
            data[-1]["error"] = (
                "Unexpected end of input, looking for %s"
                % " or ".join(repr(k.title()) for k in state.keys)
                )

        for item in data:
            if "description" in item:
                item["description"] = "\n".join(item["description"])
            for step in item.get("steps", []):
                step["instruction"] = "\n".join(step["instruction"])
                if "expected" in step:
                    step["expected"] = "\n".join(step["expected"])

        return data


    def begin(self, lc, orig, data):
        """The start state."""
        if lc.startswith("test that "):
            data.append({"name": orig})
            return self.description
        raise ParsingError("Expected 'Test that ...', not '%s'" % orig)
    begin.keys = ["Test that "]
    begin.expect_end = False


    def description(self, lc, orig, data):
        """Expecting to encounter description line(s)."""
        if lc.startswith("when ") or lc.startswith("and when "):
            data[-1].setdefault("description", [])
            data[-1]["steps"] = [{"instruction": [orig]}]
            return self.instruction
        data[-1].setdefault("description", []).append(orig)
        return self.description
    description.keys = ["when ", "and when "]
    description.expect_end = False


    def instruction(self, lc, orig, data):
        """Expecting to encounter a step instruction."""
        if lc.startswith("then "):
            data[-1]["steps"][-1]["expected"] = [orig]
            return self.expectedresult
        data[-1]["steps"][-1]["instruction"].append(orig)
        return self.instruction
    instruction.keys = ["then "]
    instruction.expect_end = False


    def expectedresult(self, lc, orig, data):
        """Expecting to encounter a step result."""
        if lc == "and":
            self._orig_and = orig
            return self.after_and
        if lc.startswith("test that "):
            data.append({"name": orig})
            return self.description
        if lc.startswith("when ") or lc.startswith("and when "):
            data[-1]["steps"].append({"instruction": [orig]})
            return self.instruction
        data[-1]["steps"][-1]["expected"].append(orig)
        return self.expectedresult
    expectedresult.keys = ["test that ", "when "]
    expectedresult.expect_end = True


    def after_and(self, lc, orig, data):
        """Expecting either a new step instruction, or continued result."""
        if lc.startswith("when "):
            data[-1]["steps"].append({"instruction": [orig]})
            return self.instruction
        data[-1]["steps"][-1]["expected"].extend([self._orig_and, orig])
        return self.expectedresult
    after_and.keys = ["when "]
    after_and.expect_end = False


from markdown import treeprocessors
from markdown.util import etree

class MarkdownBulkParser(object):
    """
    This bulk input parser takes test cases in this format:

        Test case 1 title here
        ================
        Description text here (optional)

        * which can contain bullets
        * **with formatting**
           * indentation
           * [and links](www.example.com)

        Steps
        -----
        1. Step 1 action
            * Step 1 Expected Result
        2. Step 2 action
            * Step 2 Expected Result

        ***
        ***

        Test case 2 title here
        ===============
        ...

    and create a list of case objects like this:

        {
            "name": "Test that bulk parsing works",
            "description": (
                "As a testcase administrator\n"
                "Given that I've loaded the bulk-input screen"
                ),
            "steps": [
                {
                    "instruction": (
                        "When I type a sonnet in the textarea\n"
                        "And I sing my sonnet aloud"
                        ),
                    "expected": "Then my sonnet should be parsed",
                    },
                {
                    "instruction": "And when I click the submit button",
                    "expected": "Then testcases should be created",
                    },
                {
                    "instruction": "When I am done",
                    "expected": "Then I feel satisfied",
                    },
                ]
            }

    RULES:
    ======
    * Double separator line separates cases
    * First <h1> after separator or at BOF is case name
    * Everything between that <H1> and the first occurance of <h2>Steps</h2>
      is the description
    * each numbered line after <h2>Steps</h2> is a step instruction
    * each non-numeric within a numbered step is a step expected


    """

    def parse(self, text):
        ctp = CaseTreeprocessor()
        data = "stuff?"
        return data

class CaseTreeprocessor(treeprocessors.Treeprocessor):

    def run(self, root):
        pass