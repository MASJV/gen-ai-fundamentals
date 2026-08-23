from ollama import generate

question = input("Ask a question: ")

context = """Company Overview
 
Larkspur Outfitters is an outdoor gear retailer with three physical stores and an online shop. The company was started in 2014 by two former ski instructors and now employs around 60 people across retail, warehousing, and customer support.
 
Store Locations & Hours
 
Downtown Store - 214 Maple Street
Monday to Saturday, 10am to 7pm. Sunday, 11am to 5pm.
 
Riverside Store - 88 Harbor Road
Monday to Saturday, 9am to 6pm. Closed Sundays.
 
Northgate Store - 5600 Ridge Avenue
Monday to Sunday, 10am to 8pm.
 
All stores are closed on Thanksgiving and Christmas Day. Holiday hours for other dates are posted two weeks in advance on the website.
 
Products & Categories
 
The store carries hiking and camping equipment, winter sports gear, footwear, and apparel. Product lines are split into three tiers: Trailhead (entry-level, budget-friendly), Larkspur Standard (the core in-house brand), and Summit Pro (technical gear for serious backcountry use). Rentals are available for skis, snowshoes, and tents at the Northgate and Downtown locations only.
 
Shipping & Delivery
 
Online orders over $75 ship free within the continental US. Standard shipping takes 3 to 5 business days; expedited shipping (2 business days) is available for an added fee. Orders placed before 1pm Eastern on a business day usually go out the same day. International shipping is not currently offered.
 
Returns & Exchanges
 
Items can be returned within 45 days of purchase with a receipt or order confirmation, unworn and with tags attached. Rental gear is not eligible for return. Sale items marked "final sale" cannot be returned or exchanged. Refunds are issued to the original payment method within 5 to 7 business days of the return being processed. In-store purchases can be returned at any of the three locations regardless of where they were bought; online orders can be returned by mail or in-store.
 
Membership Program
 
The Larkspur Trail Pass is a free loyalty program. Members earn 1 point per dollar spent, redeemable at 100 points per $5 off a future purchase. Trail Pass members also get early access to seasonal sales, typically 48 hours before the public. There is a paid tier, Trail Pass Plus, which costs $40 a year and adds free rentals up to twice a month and a 10% discount on repairs.
 
Repairs & Maintenance
 
The Downtown and Riverside stores have in-house repair counters for ski tuning, boot fitting, and gear patching. Turnaround is usually 3 to 5 days during the winter season and faster in the off-season. Repair pricing depends on the item; a basic ski tune runs $35, boot fitting is $25, and patch repairs on tents or jackets start at $15 depending on the size of the damage.
 
Customer Support
 
Support is available by phone, email, and live chat, Monday through Saturday, 9am to 6pm Eastern. Average response time for email is under 24 hours on weekdays. Order issues, such as wrong items or damaged shipments, are handled by the support team directly rather than requiring a return through the standard process - customers should contact support first in those cases rather than initiating a return.
 
Employment
 
Larkspur Outfitters hires seasonal staff each year starting in September for the winter season, with most seasonal roles based at the Northgate location due to its ski rental volume. Store associates receive a 30% employee discount, and seasonal staff who are asked back for a second season are eligible for full-time openings the following year."""


prompt = "Answer using this information:\n" + context + "\nQuestion: " + question

response = generate(
    model="llama3.2:1b",
    prompt=prompt,
    #stream=True, needs mulitple json objects in the response
)

print(response["response"])