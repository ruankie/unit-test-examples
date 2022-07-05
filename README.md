# Unit Test Examples
🧪 Examples of unit tests (with mocking). <br>
👨‍💻 Developed with test-driven development (TDD) by starting with tests, then writing code that makes the tests pass. <br>
🏗 Currently under construction...

# Usage
1. Clone this repo and open it:
   ```bash
   git clone https://github.com/ruankie/unit-test-examples.git
   cd unit_test_examples
   ```
1. Create a separate conda environment:
   ```bash
   conda env create -f environment.yml
   ```
1. Activate conda environment:
   ```bash
   conda activate unit_test_examples
   ```
1. Run tests:
   ```bash
   python3 unit_test_examples/tests/test_calculator.py
   ```

# TODO (Roadmap)
- [ ] Simple calculator tests (and code to make them pass)
  - [ ] Addition
  - [ ] Subtraction
  - [ ] Multiplication
  - [ ] Division
- [ ] JSON file reader tests (and code to make them pass)
  - [ ] Read file (use mocking)
  - [ ] Do something with file contents
- [ ] Use Github actions to run all tests when:
  - [ ] PR is made to merge with `main`
  - [ ] Committing
- [ ] Get code coverage to `>100%`

# References
* https://www.youtube.com/watch?v=6tNS--WetLI
* https://www.youtube.com/watch?v=WFRljVPHrkE
* https://www.youtube.com/watch?v=_OyuFg9pGQg
