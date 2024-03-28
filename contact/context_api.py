def show_us(request):
    context = dict()
    context['company'] = "The Pool Care"
    context['tel1'] = "+27 61 431 9286"
    context['tel2'] = "+27 82 514 5880"
    context['email'] = "info@thepoolcare.co.za"
    context['domain'] = "thepoolcare.co.za"
    context['address'] = """Fancourt Office Park<br>63 Felstead Rd, North Riding<br/>Randburg 2162"""
    return context