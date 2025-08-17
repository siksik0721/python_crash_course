def make_car(company, model, **kwargs):
    kwargs["company"] = company
    kwargs["model"] = model
    return kwargs


car = make_car("subaru", "outback", color="blue", tow_package="True")
print(car)
