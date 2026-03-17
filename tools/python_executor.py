import subprocess
import tempfile
from tools.base_tool import BaseTool

class PythonExecutor(BaseTool):

    name = "python_executor"
    description = "Execute Python code, install packages if needed"

    def run(self, code):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            temp_file = f.name

        try:

            result = subprocess.run(
                ["python", temp_file],
                capture_output=True,
                text=True
            )

            output = result.stdout + result.stderr

        except Exception as e:
            output = str(e)

        return output