import pytest
from wallet import Wallet
from wallet import InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.fixture
def wallet():
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 110


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)


@pytest.mark.parametrize('earned, spent, expected', [
    (30, 20, 10),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions_2(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
