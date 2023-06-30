# How to run
- clone the repo
- execute the command `pip install -r requirements.txt`.
- execute the command (to mimic in CI/CD) `locust -f tests/performance/scenario.py --headless -u 1 -r 1 --run-time 1m --host=https://jsonplaceholder.typicode.com`.
- If you want to run it using the UI run the command `locust -f tests/performance/scenario.py` instead.