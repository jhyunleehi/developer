## devstack debug 
```sh
$ git clone https://opendev.org/openstack/manila
$ pip3 install tox
$ tox
py3: install_deps> python -I -m pip install -r /home/jhyunlee/code/manila/requirements.txt -r /home/jhyunlee/code/manila/test-requirements.txt -c https://releases.openstack.org/constraints/upper/master

```




# Simple Pytest Example

This is the code for my video tutorial for getting started with Pytest.

* [Pytest Documentation](https://docs.pytest.org/en/6.2.x/getting-started.html#getstarted)
* [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)

### Install Pytest

```bash
pip install pytest
```

### Run the tests

```bash
pytest
```

### Run a specific file

```bash
pytest test_shopping_cart.py
```

### Run a specific test

```bash
pytest test_shopping_cart.py::test_can_get_total_price
```