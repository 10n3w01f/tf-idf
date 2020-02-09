import os,glob
text_data = []
for directory in os.listdir("C:/Users/sampa/Documents/dataset/movie-reviews/Dataset_Copy"):
    text_dict = {}
    i=0
    filename=("C:/Users/sampa/Documents/dataset/movie-reviews/Dataset_Copy/"+directory+"/")
#    print("**********************"+directory+"*******************")
    os.chdir(filename)
    for file in glob.glob("*.txt"):
      i+=1
      with open(file) as infile:
           text_dict={'doc_id':i,
                  'doc_data':infile.read()}
           text_data.append(text_dict)
    print(text_data)
