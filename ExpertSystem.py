import time


def hypothesis(symptoms):
    diseases = {
        ('fever', 'rash', 'runny_nose', 'cough', 'conjunctivitis'): 'measles',
        ('fever', 'rash', 'headache', 'runny_nose'): 'german_measles',
        ('fever', 'headache', 'body_ache', 'runny_nose', 'cough', 'conjunctivitis', 'chills', 'sore_throat'): 'flu',
        ('headache', 'runny_nose', 'chills', 'sore_throat', 'sneezing'): 'cold',
        ('fever', 'swollen_glands'): 'mumps',
        ('fever', 'rash', 'body_ache', 'chills'): 'chicken_pox',
        ('runny_nose', 'cough', 'sneezing'): 'common_cold',
    }
    try:
        return diseases[symptoms]
    except KeyError:
        for disease in diseases.keys():
            check = []
            for symptom in symptoms:
                if symptom in disease:
                    check.append(symptom)
            if len(check) == len(symptoms):
                return diseases[disease]
        return "Sorry, I don't seem to be able to diagnose the disease."
        


def main():
    time.sleep(0.4)
    print('-----------------------------------------------------------------')
    time.sleep(0.4)
    print('*****************************************************************')
    time.sleep(0.4)
    print("###################||| EXPERT SYSTEM |||#########################")
    time.sleep(0.4)
    print('*****************************************************************')
    time.sleep(0.4)
    print('-----------------------------------------------------------------\n\n')

    patient = input("Hi. How are you? First of all tell me your name Please : ")

    fever = input(f"{patient}, have a fever (y/n) ? ")
    rash = input(f"{patient}, have a rash (y/n) ?")
    headache = input(f"{patient}, have a headache (y/n) ? ")
    body_ache = input(f"{patient}, have a bodyache (y/n) ? ")
    runny_nose = input(f"{patient}, have a runny_nose (y/n) ? ")
    cough = input(f"{patient}, have a cough (y/n) ? ")
    conjunctivitis = input(f"{patient}, have a conjunctivitis (y/n) ? ")
    chills = input(f"{patient}, have a chills (y/n) ? ")
    sore_throat = input(f"{patient}, have a sore_throat (y/n) ? ")
    sneezing = input(f"{patient}, have a sneezing (y/n) ? ")
    swollen_glands = input(f"{patient}, have a swollen_glands (y/n) ? ")

    symptoms = []
    if fever == 'y':
        symptoms.append('fever')
    if rash == 'y':
        symptoms.append('rash')
    if headache == 'y':
        symptoms.append('headache')
    if body_ache == 'y':
        symptoms.append('body_ache')
    if runny_nose == 'y':
        symptoms.append('runny_nose')
    if cough == 'y':
        symptoms.append('cough')
    if conjunctivitis == 'y':
        symptoms.append('conjunctivitis')
    if chills == 'y':
        symptoms.append('chills')
    if sore_throat == 'y':
        symptoms.append('sore_throat')
    if sneezing == 'y':
        symptoms.append('sneezing')
    if swollen_glands == 'y':
        symptoms.append('swollen_glands')

    disease = hypothesis(tuple(symptoms))
    if disease == "Sorry, I don't seem to be able to diagnose the disease.":
        print("\nSorry, I don't seem to be able to diagnose the disease.")
    else:
        print(f"\n{patient}, you probably have {disease}.\n\n")
        time.sleep(0.4)
        print('*****************************************************************')
        time.sleep(0.4)
        print("################||| THANK YOU FOR USING ME |||#####################")
        time.sleep(0.4)
        print('*****************************************************************')


if __name__ == '__main__':
    main()
