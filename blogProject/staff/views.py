from django.shortcuts import render

employees = [
  {
    "id": 0,
    "name": "Lawrence",
    "surname": "Estrada",
    "age": 37,
    "gender": "male",
    "email": "lawrenceestrada@lovepad.com",
    "phone": "+1 (937) 549-3316",
    "address": "131 Will Place, Chapin, New Hampshire, 6839"
  },
  {
    "id": 1,
    "name": "Stafford",
    "surname": "Whitney",
    "age": 27,
    "gender": "male",
    "email": "staffordwhitney@lovepad.com",
    "phone": "+1 (861) 427-3475",
    "address": "145 Pine Street, Broadlands, North Dakota, 7831"
  },
  {
    "id": 2,
    "name": "Herrera",
    "surname": "Lawson",
    "age": 39,
    "gender": "male",
    "email": "herreralawson@lovepad.com",
    "phone": "+1 (892) 516-3955",
    "address": "564 Rapelye Street, Fredericktown, Illinois, 3289"
  },
  {
    "id": 3,
    "name": "Alston",
    "surname": "Campos",
    "age": 36,
    "gender": "male",
    "email": "alstoncampos@lovepad.com",
    "phone": "+1 (822) 557-2659",
    "address": "365 Revere Place, Tecolotito, Palau, 9404"
  },
  {
    "id": 4,
    "name": "Lynette",
    "surname": "Hogan",
    "age": 37,
    "gender": "female",
    "email": "lynettehogan@lovepad.com",
    "phone": "+1 (807) 517-2968",
    "address": "845 Herzl Street, Sutton, Virginia, 8688"
  },
  {
    "id": 5,
    "name": "Myrtle",
    "surname": "Gilbert",
    "age": 39,
    "gender": "female",
    "email": "myrtlegilbert@lovepad.com",
    "phone": "+1 (974) 539-2435",
    "address": "394 McKibbin Street, Deltaville, Idaho, 652"
  }
]


def get_employees(request):
    return render(request, 'staff/index.html', {'employees': employees})


def get_employee(request):
    pass