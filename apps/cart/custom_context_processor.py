def importe_total_carro(request):
    total = 87
    if request.user.is_authenticated:
        print('I got to this point')
        for key, value in request.session['carro'].items():
        #for key, value in request.session['carro'].items():
            total = total + (float(value['precio']) * value['cantidad'])
    return {'importe_total' : total}
