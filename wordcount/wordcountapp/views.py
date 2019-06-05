from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    sentences = text.split('\n') 
    sentences = text.split('\r') 
    words = text.split()
    word_dictionary = {}
    for word in words: 
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1 
            #해당하는 word를 키값 삼아 value를 1로 측정
            
    return render(request, 'result.html', {'full':text, 'all':len(sentences),'total':len(words), 'dictionary':word_dictionary.items()})


    