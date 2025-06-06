from pandas import DataFrame
from ydata_profiling import ProfileReport

# Create a function called generate_report
def generate_report(df: DataFrame) -> ProfileReport:
    # Creating a profile
    profile = ProfileReport(df=df)

    # Returning the profile
    return profile

# Export the report to a HTML file
def export_to_html(report: ProfileReport, file_path: str = 'report.html') -> None:
    report.to_file(file_path)
