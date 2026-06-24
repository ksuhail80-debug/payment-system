ipmort random

def get_payment_details():
  print("step 1: Getting payment details")
  amount = int(input("enter amount: "))
  user = input("Enter username: ")
  return amount, user
  def validate_apyment(amount):
    print("step 2: validating payment")

if amount <=0:
  return false, "Invalid amount"
  return True, "Valid"
  def create_Payment_request(user, amount):
    print("step 3: creating payment request")
    return {
      "user": user,
      "amount": amount,
      "status": "created"
    }
    def payment_gateway)Payment_request):
      print("step 4: calling payment gateway")

      success = random.choice([True, False])

if success:
  return "success"
else:
  return "failure"

def send_response(status):
  print("step 5: sending response")

if status == "success":
  print("payment successful")
else:
  print(Payment failed")

def payment_flow()
  amount, user = get_payment_details()

  valid, message = validate_payment(amount)

if not valid:
  print(message)
  return

request = create_payment_request(user, amount)

status = payment_gateway(request)

send_response(status)

payment_flow()
