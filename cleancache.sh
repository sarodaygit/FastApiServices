find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . | grep -E "(\.pytest_cache)" | xargs rm -rf