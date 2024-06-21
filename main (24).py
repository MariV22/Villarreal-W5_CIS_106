def main():
  # Initialize variables
  total_discount = 0.0

  # Prompt user to start the program
  continue_prompt = input("Do you want to enter item data? (Yes/No): ").strip().lower()

  # Continue while loop if user answers 'yes'
  while continue_prompt == "yes":
      # Prompt for item data
      quantity = int(input("Enter quantity of the item: "))
      price = float(input("Enter price per item: "))

      # Calculate extended price
      extended_price = quantity * price

      # Determine discount based on extended price
      if extended_price > 10000.00:
          discount_percent = 0.25
      else:
          discount_percent = 0.10

      # Calculate discount amount
      discount_amount = extended_price * discount_percent

      # Calculate total amount after discount
      total = extended_price - discount_amount

      # Accumulate total discount
      total_discount += discount_amount

      # Display order details
      print(f"Extended Price: ${extended_price:.2f}")
      print(f"Discount Amount: ${discount_amount:.2f}")
      print(f"Total Amount after Discount: ${total:.2f}")

      # Prompt user again to continue or not
      loop_prompt = input("Do you want to enter data for another item? (Yes/No): ").strip().lower()

      # If user says 'no' to continue the loop, break out
      if loop_prompt != "yes":
          break

      # Prompt user again to continue the whole program
      continue_prompt = input("Do you want to enter more item data? (Yes/No): ").strip().lower()

  # Display total discount amount
  print("\nSummary:")
  print(f"Total Discount Amount: ${total_discount:.2f}")

# Run the main function
if __name__ == "__main__":
  main()