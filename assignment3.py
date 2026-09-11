import functools
import uuid
from abc import ABC, abstractmethod
from datetime import datetime


# Step 2: Receipt Class
class Receipt:
    def __init__(self, amount: float, method: str, status: str):
        self.txn_id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[RECEIPT] ID: {self.txn_id} | Method: {self.method} | Amount: ${self.amount:.2f} | Status: {self.status} | Date: {self.timestamp}"

    def __repr__(self):
        return f"Receipt(txn_id='{self.txn_id}', amount={self.amount}, status='{self.status}')"


# Step 3: Abstract PaymentStrategy Interface
class PaymentStrategy(ABC):
    name: str = "Generic Payment"

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def pay(self, amount: float) -> Receipt:
        pass

    def _make_receipt(self, amount: float, status: str) -> Receipt:
        return Receipt(amount=amount, method=self.name, status=status)


# Step 4-7: Concrete Strategy Classes
class CreditCardPayment(PaymentStrategy):
    name = "Credit Card"

    def __init__(self, card_number: str, cvv: str, expiry: str):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate(self) -> bool:
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def pay(self, amount: float) -> Receipt:
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")


class PayPalPayment(PaymentStrategy):
    name = "PayPal"

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def validate(self) -> bool:
        return "@" in self.email and len(self.password) >= 6

    def pay(self, amount: float) -> Receipt:
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")


class UPIPayment(PaymentStrategy):
    name = "UPI"

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def validate(self) -> bool:
        return "@" in self.upi_id

    def pay(self, amount: float) -> Receipt:
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")


class NetBankingPayment(PaymentStrategy):
    name = "Net Banking"

    def __init__(self, bank_name: str, account_number: str):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self) -> bool:
        return len(self.bank_name) > 0 and len(self.account_number) >= 8

    def pay(self, amount: float) -> Receipt:
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")


# Step 8: Logging Decorator
def log_transaction(func):
    @functools.wraps(func)
    def wrapper(self, amount, *args, **kwargs):
        method_name = self.strategy.name if self.strategy else "Unknown"
        print(f"[LOG] Attempting payment of ${amount:.2f} using {method_name}...")
        result = func(self, amount, *args, **kwargs)
        print(f"[LOG] Transaction finished with status: {result.status}\n")
        return result

    return wrapper


# Step 9-11: PaymentProcessor (Context Class)
class PaymentProcessor:
    _registry = {}  # Class attribute mapping strategy keys to strategy classes

    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        print(f"[CONFIG] Switched strategy to: {strategy.name}")
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount: float) -> Receipt:
        if not self.strategy:
            raise ValueError("No payment strategy configured.")
        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, key: str, strategy_cls: type):
        cls._registry[key] = strategy_cls
        print(f"[REGISTRY] Registered strategy '{key}' -> {strategy_cls.__name__}")

    @classmethod
    def create(cls, key: str, **kwargs):
        if key not in cls._registry:
            raise KeyError(f"Strategy '{key}' is not registered.")
        strategy_cls = cls._registry[key]
        return cls(strategy_cls(**kwargs))

    @classmethod
    def available_methods(cls):
        return list(cls._registry.keys())


# Step 12-16: Demonstration & Driver Code
if __name__ == "__main__":
    # Register available strategies dynamically
    PaymentProcessor.register_strategy("upi", UPIPayment)
    PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
    PaymentProcessor.register_strategy("paypal", PayPalPayment)
    PaymentProcessor.register_strategy("net_banking", NetBankingPayment)

    print(
        f"\nAvailable Payment Methods: {PaymentProcessor.available_methods()}\n"
    )

    # 1. Create a processor via Factory method using UPI
    processor = PaymentProcessor.create("upi", upi_id="user@okbank")
    receipt1 = processor.process_payment(1500.00)
    print(receipt1)

    # 2. Switch strategy dynamically at runtime using set_strategy()
    processor.set_strategy(
        CreditCardPayment("1234567812345678", "123", "12/28")
    )
    receipt2 = processor.process_payment(250.50)
    print(receipt2)

    # 3. Switch to Net Banking
    processor.set_strategy(
        NetBankingPayment("NationalBank", "9876543210")
    )
    receipt3 = processor.process_payment(5000.00)
    print(receipt3)

    # 4. Intentionally invalid credentials test (Failed Receipt)
    processor.set_strategy(UPIPayment("invalid_upi_format"))
    receipt4 = processor.process_payment(100.00)
    print(receipt4)