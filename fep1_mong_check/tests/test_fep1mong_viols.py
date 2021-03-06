from ..fep1_mong_check import model_path, FEP1MongCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest
import os


def test_JUL3019A_viols(answer_store, test_root):
    answer_data = os.path.join(os.path.dirname(__file__), "answers",
                               "JUL2919A_viol.json")
    fm_rt = RegressionTester(FEP1MongCheck, model_path,
                             "fep1_mong_test_spec.json",
                             test_root=test_root, sub_dir='viols')
    fm_rt.check_violation_reporting("JUL2919A", answer_data,
                                    answer_store=answer_store)