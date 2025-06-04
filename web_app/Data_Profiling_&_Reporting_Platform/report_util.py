from pandas import DataFrame
from ydata_profiling import ProfileReport

# Create a function called generate_report
def generate_report(df: DataFrame) -> ProfileReport:
    # Creating a profile
    profile = ProfileReport(df=df)

    # Returning the profile
    return profile