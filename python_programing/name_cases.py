name = "eric"
message = '"Hello '+ name.title() + ',would you like to learn some Python today?"'
print(message)

message_famous = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(message_famous)

famous_name = "    \n     albert einstein"
famous_other = ' once said, “A person who never made a mistake never tried anything new.”'
famous_message = famous_name.title().strip()+famous_other
print(famous_message)
print(famous_name.title())