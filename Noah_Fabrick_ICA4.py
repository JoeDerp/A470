import Noah_Fabrick_ICA3 as transport

car1 = transport.cars('car',400,4,'Hyundai','Santa Fe','blue')
car2 = transport.cars('car',400,4,'Chevrolet','Lumina','white')
plane1 = transport.planes('airplane',9000,800,'Emirates','Airbus','A380')

print(plane1)
print(car1 == plane1)
print(car1 == car2)
