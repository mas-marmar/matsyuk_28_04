from django.shortcuts import render

def calculator(request):
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation', '+')
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    error = 'Низя дилить на нуль!'
                else:
                    result = num1 / num2
                    
        except (ValueError, TypeError):
            error = 'ашипка'
    
    return render(request, 'calculator.html', {
        'result': result,
        'error': error,
    })