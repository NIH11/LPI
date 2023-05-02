from django.shortcuts import render, HttpResponse
from Home.models import Calculation

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Homepage")

def calculator(request):
       #return HttpResponse("This is calculator")
   return render(request, 'calculator.html')
    
def services(request):
       #return HttpResponse("This is our services")
   return render(request, 'services.html')

def Aboutus(request):
       #return HttpResponse("This is Aboutus")
   return render(request, 'Aboutus.html')

def Contactus(request):
       #return HttpResponse("This is Contactus")
   return render(request, 'Contactus.html')

from django.shortcuts import render
from Home.models import Calculation

def calculator(request):
    result=''
    if request.method == 'POST':
        num1 = eval(request.POST.get('num1'))
        num2 = eval(request.POST.get('num2'))
        operator = request.POST.get('operator')
        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'
        print(result)
        # save calculation to database
        calculation = Calculation(num1=num1, num2=num2, operator=operator, result=result)
        calculation.save()
        # render result template with context
        context = {
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'result': result,
        }
        #return render(request, 'result.html',context)

    return render(request, 'calculator.html',{'result':result})

import pandas as pd
from django.shortcuts import render
from Home.models import Pollutant
import csv
import os



#def LPI(request):
    #lpi =''    
    # Replace 'path/to/your/excel/file.xlsx' with the actual path to your Excel file
    #df = pd.read_excel('D:\LPI\LPI_Index\LPI.xlsx')

    # Get the concentration and background values as lists
    #concentrations = df['Concentration'].tolist()
    #pollutantweight = df['Pollutantweight'].tolist()
            
    #if request.method == 'POST':
        # Get the list of concentrations and backgrounds from the submitted form data
        #concentrations = []
        #pollutantweight = []
        #for i in range(1,100):
            
            #concentration_str = request.POST.get(f'concentration_{i}')
            #pollutantweight_str = request.POST.get(f'pollutantweight_{i}')
            #if concentration_str is not None:
                #concentrations.append(float(concentration_str))
            #if pollutantweight_str is not None:
                #pollutantweight.append(float(pollutantweight_str))
        
       # Calculate the numerator
    #numerator = sum([c * b for c, b in zip(concentrations, pollutantweight)])

    # Calculate the denominator
    #denominator = sum(pollutantweight)

    # Calculate the LPI
    #lpi = numerator / denominator
    #print(lpi)
        
        # Render the result in a template
    #context = {'lpi': lpi}
    #return render(request, 'Lpiindex.html', context)

    #Return the LPI value as a response
    #return render(request, 'Lpiindex.html',{'lpi':lpi})
    #return HttpResponse(f"The leachate pollution index is: {lpi:.2f}")
        
    
    # If the request method is not POST, render the form template
    #else:
        #return HttpResponse(f"The leachate pollution index is: {lpi:.2f}")
     #return render(request, 'Lpiindex.html',{'lpi':lpi})
     
 
# Dictionary to map fixed parameter names to CSV column names

def LPI(request):
    lpi=''
    if request.method == 'POST':
        # Get the parameter names and values from the form
        parameters = request.POST.getlist('parameter')
        values = [float(v) for v in request.POST.getlist('value')]

        # Read the background and concentration values from a static CSV file
        with open('D:\LPI\LPI_Index\LPI_Index/static/concentrations.csv') as f:
            reader = csv.DictReader(f)
            backgrounds = {}
            concentrations = {}
            for row in reader:
                parameter = row['parameter']
                if parameter in parameters:
                    backgrounds[parameter] = float(row['background'])
                    concentrations[parameter] = float(row['concentration'])

        # Calculate the numerator
        numerator = sum([concentrations[parameters[i]] * backgrounds[parameters[i]] for i in range(len(parameters))])

        # Calculate the denominator
        denominator = sum(backgrounds.values())

        # Calculate the LPI
        lpi = numerator / denominator
        
        # Format the LPI to three decimal places
        formatted_lpi = "{:.3f}".format(lpi)
        
        print(lpi)
                        
        #Return the LPI value as a response
        return render(request, 'Lpiindex.html',{'lpi':formatted_lpi})
        # Render the result in a template
        #context = {'lpi': lpi}
        #return render(request, 'result.html', context)
    
    else: 
        # Render the form template
        return render(request, 'Lpiindex.html')
    
    #LPI Sub indices
    
def lpiorganic(request):
     lpiorganic=''
    
     if request.method == 'POST':
        # Get the parameter names and values from the form
        parameters = request.POST.getlist('parameter')
        values = [float(v) for v in request.POST.getlist('value')]

        # Read the background and concentration values from a static CSV file
        with open('D:\LPI\LPI_Index\LPI_Index/static/Lpiorganic.csv') as f:
            reader = csv.DictReader(f)
            backgrounds = {}
            concentrations = {}
            for row in reader:
                parameter = row['parameter']
                if parameter in parameters:
                    backgrounds[parameter] = float(row['background'])
                    concentrations[parameter] = float(row['concentration'])

        # Calculate the numerator
        numerator = sum([concentrations[parameters[i]] * backgrounds[parameters[i]] for i in range(len(parameters))])

        # Calculate the denominator
        denominator = sum(backgrounds.values())

        # Calculate the LPI
        lpiorganic = numerator / denominator
        
        # Format the LPI to three decimal places
        formatted_lpiorganic = "{:.3f}".format(lpiorganic)
        
        print(lpiorganic)
                        
        #Return the LPI value as a response
        return render(request, 'Lpior.html',{'lpiorganic':formatted_lpiorganic})
        # Render the result in a template
        #context = {'lpi': lpi}
        #return render(request, 'result.html', context)
    
     else: 
        # Render the form template
        return render(request, 'Lpior.html')
    
    # lpi inorganic
def lpiinorganic(request):
     lpiinorganic=''
    
     if request.method == 'POST':
        # Get the parameter names and values from the form
        parameters = request.POST.getlist('parameter')
        values = [float(v) for v in request.POST.getlist('value')]

        # Read the background and concentration values from a static CSV file
        with open('D:\LPI\LPI_Index\LPI_Index/static/Lpiinorganic.csv') as f:
            reader = csv.DictReader(f)
            backgrounds = {}
            concentrations = {}
            for row in reader:
                parameter = row['parameter']
                if parameter in parameters:
                    backgrounds[parameter] = float(row['background'])
                    concentrations[parameter] = float(row['concentration'])

        # Calculate the numerator
        numerator = sum([concentrations[parameters[i]] * backgrounds[parameters[i]] for i in range(len(parameters))])

        # Calculate the denominator
        denominator = sum(backgrounds.values())

        # Calculate the LPI
        lpiinorganic = numerator / denominator
        
        # Format the LPI to three decimal places
        formatted_lpiinorganic = "{:.3f}".format(lpiinorganic)
        
        print(lpiinorganic)
                        
        #Return the LPI value as a response
        return render(request, 'Lpiinor.html',{'lpiinorganic':formatted_lpiinorganic})
        # Render the result in a template
        #context = {'lpi': lpi}
        #return render(request, 'result.html', context)
    
     else: 
        # Render the form template
        return render(request, 'Lpiinor.html')
    
    #lpiheavymetals
def lpiheavymetals(request):
     lpiheavymetals=''
    
     if request.method == 'POST':
        # Get the parameter names and values from the form
        parameters = request.POST.getlist('parameter')
        values = [float(v) for v in request.POST.getlist('value')]

        # Read the background and concentration values from a static CSV file
        with open('D:\LPI\LPI_Index\LPI_Index/static/Lpimetals.csv') as f:
            reader = csv.DictReader(f)
            backgrounds = {}
            concentrations = {}
            for row in reader:
                parameter = row['parameter']
                if parameter in parameters:
                    backgrounds[parameter] = float(row['background'])
                    concentrations[parameter] = float(row['concentration'])

        # Calculate the numerator
        numerator = sum([concentrations[parameters[i]] * backgrounds[parameters[i]] for i in range(len(parameters))])

        # Calculate the denominator
        denominator = sum(backgrounds.values())

        # Calculate the LPI
        lpiheavymetals = numerator / denominator
        
        # Format the LPI to three decimal places
        formatted_lpiheavymetals = "{:.3f}".format(lpiheavymetals)
        
        print(lpiheavymetals)
                        
        #Return the LPI value as a response
        return render(request, 'Lpimetals.html',{'lpiheavymetals':formatted_lpiheavymetals})
        # Render the result in a template
        #context = {'lpi': lpi}
        #return render(request, 'result.html', context)
    
     else: 
        # Render the form template
        return render(request, 'Lpimetals.html')    
    

    
