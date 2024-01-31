import Noah_Fabrick_ICA3 as transport

rockets = transport.transportation('rocketship',1500,5)
car1 = transport.cars('car',400,4,'Hyundai','Santa Fe','blue')
car2 = transport.cars('car',400,4,'Chevrolet','Lumina','white')
plane1 = transport.planes('airplane',9200,853,'Emirates','Airbus','A380')

print(rockets)
print(plane1)
print(car1 == plane1)
print(car1 == car2)
car1.whatColor()
car2.whatBrand()
