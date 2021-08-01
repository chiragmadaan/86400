Setup:
1. Open terminal
2. Navigate to the project directory
3. Activate/Source the python virtual environment using command: source ../venv/bin/activate
4. Start the appium server
5. Edit config/driver.ini with the correct details about appium server and test capabilities
6. Launch the emulator
6. Run tests using command: python3 -m pytest tests -v --html report.html
    6.1 Testing framework 'pytest' is being used
    6.2 pytest-html package is being used to generate html report
7. You can also run the same tests on a different APK using the --app command line argument
    7.1 Command: python3 -m pytest tests -v --app <path_to_apk>
    7.2 twitter APK file could not be included in the zip file because of the file size limitation of hackerrank. ZIP file could not be more than 50 MB but the twitter apk file was 100+ MB. So please download the twitter APK before running the tests.

File structure:
1. config/driver.ini file contains the configuration details
2. pages directory contains page classes
3. conftest.py contains the fixture functions used for setup and tear down of the drivers (Equivalent of BeforeTest and AfterTest in TestNG/Junit)
4. test_fresh_launch.py contains 3 tests
    4.1 First test verifies the first screen
    4.2 Second test clicks on the create account button and verifies the create account screen
    4.3 Third test clicks on the create account button on first screen then clicks back on the second screen and verifies that first screen is shown again
5. util directory contains utility classes that are used to locate or click elements etc

Disclaimer: Sometimes a different version of the welcome screen shown on launch. Tests are written for one type of screen so the test will fail when the other version of the screen is shown. Try running the tests again if the fail.