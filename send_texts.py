from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC4ca1184c2d64dd32b8a0c2f610374b1b"
# Your Auth Token from twilio.com/console
auth_token  = "89f01dc2e694a55c0e1f2103a248dc4a"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+358400239522‬",
    from_="+12013081901",
    body="Daniela on paras!")

print(message.sid)