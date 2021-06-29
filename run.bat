rem pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=./Report/report.html ./testCases/ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=./Report/report.html ./testCases/ --browser chrome
pytest -v -s -m "regression" --html=./Report/report.html testCases/ --browser chrome