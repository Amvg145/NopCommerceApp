pip install -r requirements.txt
pytest -v -s --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=Reports\Report.html testCases\ --browser chrome
rem pytest -v -s -m "regression" --html=Reports\Report.html testCases\ --browser chrome