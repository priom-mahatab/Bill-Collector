us_bills = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
monetary_charged = float(input("Amount charged: "))
monetary_given = float(input("Amount given: "))

def finding_nearest_note(diff):
    closest_val = 0
    for bill in us_bills:
        if bill <= diff:
            return bill
    return 0

def bill_collector():
    amount_returned = 0
    returned_notes = {}
    difference = round(monetary_given - monetary_charged, 2)

    if monetary_charged == monetary_given:
        return "No money required"

    elif monetary_charged > monetary_given:
        return f"You need to pay ${monetary_charged-monetary_given:.2f} more"

    while difference > 0:
        large_note = finding_nearest_note(difference)
        if large_note == 0:
            break

        note_count = int(difference // large_note)
        returned_notes[large_note] = note_count
        difference = round(difference - note_count * large_note, 2)
    return returned_notes

change = bill_collector()

if isinstance(change, dict):
    print("Change to return:")
    for bill, count in change.items():
        if bill >=1 :
            print(f"${bill}: {count}")
        else:
            print(f"{int(bill*100)}¢: {count}")
else:
    print(change)