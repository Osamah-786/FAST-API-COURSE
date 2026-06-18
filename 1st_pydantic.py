from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated # Optional tab use kiyan jaata hai jab use mai rakhna hota hai.jaise ki kisi ko allergy nhi hai or usse batana nhi hai

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="name of the patient",description="Give the name of the patient less than 50 chars",examples=["nistish","osamah"])]
    age:int
    weight:float=Field(gt=0)
    married:Annotated[bool,Field(default=None,description="Is The Patient Married Or Not")]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details:Dict[str,str]
    email:EmailStr
    LinkedIn:AnyUrl
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print("Inserted")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print("Updated")

patient_info = {
    "name": "nitish",
    "age": 24,
    "weight": 75.60,
    "married": True,
    "allergies": ["ChickenPoks"],
    "contact_details": {
        "phone": "123334567890"
        
    },
    "email": "shaikh@gmail.com"
,
    "LinkedIn": "https://linkedin.com/in/12344"

}
patient1=Patient(**patient_info)
insert_patient_data(patient1)