from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
import joblib
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    if not request.user.is_authenticated:
        print("User is not authenticated")
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if the username is already taken
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username is already taken. Please choose a different one.')
            return redirect('signup')  # Redirect back to the signup page with an error message

        # Check if the passwords match
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('signup')  # Redirect back to the signup page with an error message

        # Create the user
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()

        messages.success(request, 'User has been created successfully.')
        return redirect('login')  # Redirect to the home page or login page

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
        print(username,pass1)

    return render(request,'login.html')

def LiverPage(request):
    return render(request,'liver.html')

def LiverResult(request):
    # Load the pre-trained model
    cls = joblib.load("finalized_model.sav")

    # Collect input values from the request
    age = float(request.GET.get('age', 0.0))  # Default to 0.0 if not provided or invalid
    gen = float(request.GET.get('gen', 0.0))  # Modify the type conversion based on your data types
    bil = float(request.GET.get('bil', 0.0))
    dbil = float(request.GET.get('dbil', 0.0))
    aph = float(request.GET.get('aph', 0.0))
    alam = float(request.GET.get('alam', 0.0))
    asam = float(request.GET.get('asam', 0.0))
    tp = float(request.GET.get('tp', 0.0))
    alb = float(request.GET.get('alb', 0.0))
    algl = float(request.GET.get('algl', 0.0))

    # Create a list of numeric input values
    lis = [age, gen, bil, dbil, aph, alam, asam, tp, alb, algl]

    # Print the input list for debugging
    print(lis)

    # Make predictions using the model
    ans = cls.predict([lis])

    # Render the result template with the prediction
    return render(request, "liver_result.html", {'ans': ans, 'lis':lis})

def HeartPage(request):
    return render(request,'heart.html')
def HeartResult(request):
    # Load the pre-trained model
    cls = joblib.load("heartdisease2.sav")

    # Collect input values from the request
    age = float(request.GET.get('age', 0.0))  # Default to 0.0 if not provided or invalid
    sex = float(request.GET.get('sex', '')) # Modify the type conversion based on your data types
    chestPainType = float(request.GET.get('chestPainType', 0.0))
    restingBP = float(request.GET.get('restingBP', 0.0))
    cholesterol = float(request.GET.get('cholesterol', 0.0))
    fastingBS = float(request.GET.get('fastingBS', 0.0))
    restingECG = float(request.GET.get('restingECG', ''))
    maxHR = float(request.GET.get('maxHR', 0.0))
    exerciseAngina = float(request.GET.get('exerciseAngina', ''))
    oldpeak = float(request.GET.get('oldpeak', 0.0))
    stSlope = float(request.GET.get('stSlope',0.0))

    # Create a list of numeric input values
    lis = [age, sex, chestPainType, restingBP, cholesterol, fastingBS, restingECG, maxHR, exerciseAngina, oldpeak,stSlope]

    # Print the input list for debugging
    print(lis)

    # Make predictions using the model
    ans = cls.predict([lis])

    # Render the result template with the prediction
    return render(request, "heart_result.html", {'ans': ans, 'lis':lis})

def BreastPage(request):
    return render(request,'breast.html')
def BreastResult(request):
    # Load the pre-trained model
    cls = joblib.load("breastcancer.sav")

    # Collect input values from the request
    concavePointsMean = float(request.GET.get('concavePointsMean', 0.0))  # Default to 0.0 if not provided or invalid
    areaMean = float(request.GET.get('areaMean', 0.0))  # Modify the type conversion based on your data types
    radiusMean = float(request.GET.get('radiusMean', 0.0))
    perimeterMean = float(request.GET.get('perimeterMean', 0.0))
    concavityMean = float(request.GET.get('concavityMean', 0.0))


    # Create a list of numeric input values
    lis = [concavePointsMean, areaMean, radiusMean, perimeterMean, concavityMean]

    # Print the input list for debugging
    print(lis)

    # Make predictions using the model
    ans = cls.predict([lis])

    # Render the result template with the prediction
    return render(request, "breast_result.html", {'ans': ans, 'lis':lis})


def ParkinsonPage(request):
    return render(request,'parkinson.html')

def ParkinsonResult(request):
    # Load the pre-trained model
    cls = joblib.load("parkisnon.sav")

    # Collect input values from the request
    mdvpFo = float(request.GET.get('mdvpFo', 0.0))  # Default to 0.0 if not provided or invalid
    mdvpFhi = float(request.GET.get('mdvpFhi', 0.0))  # Modify the type conversion based on your data types
    mdvpFlo = float(request.GET.get('mdvpFlo', 0.0))
    mdvpJitter = float(request.GET.get('mdvpJitter', 0.0))
    mdvpJitterAbs = float(request.GET.get('mdvpJitterAbs', 0.0))
    mdvpRAP = float(request.GET.get('mdvpRAP', 0.0))
    mdvpPPQ = float(request.GET.get('mdvpPPQ', 0.0))
    jitterDDP = float(request.GET.get('jitterDDP', 0.0))
    mdvpShimmer = float(request.GET.get('mdvpShimmer', 0.0))
    mdvpShimmerdB = float(request.GET.get('mdvpShimmerdB', 0.0))
    shimmerAPQ3 = float(request.GET.get('shimmerAPQ3', 0.0))
    shimmerAPQ5 = float(request.GET.get('shimmerAPQ5', 0.0))
    mdvpAPQ = float(request.GET.get('mdvpAPQ', 0.0))
    shimmerDDA = float(request.GET.get('shimmerDDA', 0.0))
    nhr = float(request.GET.get('nhr', 0.0))
    hnr = float(request.GET.get('hnr', 0.0))
    rpde = float(request.GET.get('rpde', 0.0))
    dfa = float(request.GET.get('dfa', 0.0))
    spread1 = float(request.GET.get('spread1', 0.0))
    spread2 = float(request.GET.get('spread2', 0.0))
    d2 = float(request.GET.get('d2', 0.0))
    ppe = float(request.GET.get('ppe', 0.0))

    # Create a list of numeric input values
    lis = [mdvpFo, mdvpFhi, mdvpFlo, mdvpJitter, mdvpJitterAbs, mdvpRAP, mdvpPPQ, jitterDDP, mdvpShimmer,
           mdvpShimmerdB, shimmerAPQ3, shimmerAPQ5, mdvpAPQ, shimmerDDA, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]

    # Print the input list for debugging
    print(lis)

    # Make predictions using the model
    ans = cls.predict([lis])

    # Render the result template with the prediction
    return render(request, "parkinson_result.html", {'ans': ans, 'lis': lis})

def DiabetesPage(request):
    return render(request,'diabetes.html')

def DiabetesResult(request):
    # Load the pre-trained model
    cls = joblib.load("diabetes_model.sav")

    # Collect input values from the request
    pregnancies = float(request.GET.get('pregnancies', 0.0))  # Default to 0.0 if not provided or invalid
    glucose = float(request.GET.get('glucose',0.0))
    bloodPressure = float(request.GET.get('bloodPressure', 0.0))  # Modify the type conversion based on your data types

    skinThickness = float(request.GET.get('skinThickness', 0.0))
    insulin = float(request.GET.get('insulin', 0.0))
    bmi = float(request.GET.get('bmi', 0.0))
    dpf = float(request.GET.get('dpf', 0.0))
    age = float(request.GET.get('age', 0.0))

    # Create a list of numeric input values
    lis = [pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, dpf, age]

    # Print the input list for debugging
    print(lis)

    # Make predictions using the model
    ans = cls.predict([lis])

    # Render the result template with the prediction
    return render(request, "diabetes_result.html", {'ans': ans, 'lis': lis})


def LogoutPage(request):
    logout(request)
    return redirect("login")

