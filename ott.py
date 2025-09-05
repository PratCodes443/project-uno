class Netflix:
    def __init__(self,user_name,user_id,fee):
        self.name=user_name
        self.id=user_id
        self.fee=fee
    
    def sub_label(self):
        if self.fee == 999:
            print(f"subscription label of user:{self.name},of id:{self.id} is Gold and screen number is 4")
        elif self.fee == 599:
            print(f"subscription label of user:{self.name},of id:{self.id} is Silver and screen number is 2")
        elif self.fee == 299:
            print(f"subscription label of user:{self.name},of id:{self.id} is Bronze and screen number is 1")
        else:
            print("user has no subscription")

name=input("Enter username: ")
userid=int(input("Enter id: "))
fee=int(input("Enter fees: "))

user1=Netflix(name,userid,fee)
user1.sub_label()