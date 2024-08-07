## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()


from crewai_tools import PDFSearchTool

# Initialize the tool allowing for any PDF content search if the path is provided during execution
tool_1 = PDFSearchTool()

# OR

# Initialize the tool with a specific PDF path for exclusive search within that document
tool_1 = PDFSearchTool(pdf='report.pdf')