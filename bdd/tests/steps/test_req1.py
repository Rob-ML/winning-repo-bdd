import os
import unittest

import pytest
from pyspark import Row
from pyspark.sql import SparkSession
from pytest_bdd import scenario, given, when, then, parsers

from bdd.req1 import get_total_number_of_clients

dir_path = os.path.dirname(os.path.abspath(__file__))

spark = SparkSession.builder.master("local").appName("TestReq1").getOrCreate()


@scenario("../features/req1.feature", "Get total number of clients")
def test_get_total_number_of_clients():
    pass
#
# @scenario("../features/req1.feature", "Get the subtotals for clients in the Transportation sector")
# def test_get_subtotal_for_clients_in_transport():
#     pass
@pytest.fixture
@given("the source client details data")
def source_client_details_data():
    return spark.read.option("header", True).option("inferSchema", True).csv(
        dir_path + "/../fixtures/client_details.csv"
    )

@pytest.fixture
@when("the client details is passed to the get total number of clients process")
def get_total_number_of_clients_result(source_client_details_data):
    return get_total_number_of_clients()

@then("the process should return the sum of the distinct ids")
def shows_sum_of_clients(get_total_number_of_clients_result):
    print(get_total_number_of_clients_result)
    actual = get_total_number_of_clients_result
    expected = 5000
    assert expected == actual


if __name__ == '__main__':
    unittest.main()