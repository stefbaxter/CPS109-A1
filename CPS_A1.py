# PROBLEM OUTLINE: I've decided to use this assignment as a way to simultaneously study for my french midterm. French is my second language, and it has many rules, most of them without good reason.
# I've created a verb conjugation generator for the verb tense "passé composé". The user will enter the subject (je, tu, il/elle, nous, vous, ils/elles) for which the english equivalent is (me, you, them, we, etc.)
# The user will then enter the verb without conjugation (in french we say this is "à l'infinitif". Based on the subject they entered, they may be prompted to specify if the subject is feminine or masculine.
# "We" in french is "nous", but if all of "we" are female then some conjugations will be different.
# Please note this program works for very 'standard' verbs, which in french are ones ending in "-er" when not conjugated. There are just too many rules to include any more types of verbs, even for a single verb tense, in this program.
# I understand this may be a bit difficult to grade if you are not fimiliar with the rules of the passé composé verb tense. I will try to give you as much context as possible:
# French has two auxiliaries which are used to conjugate verbs, "être" and "avoir". Most use "avoir", in which case conjugation is very easy, since all 'standard' verbs for which this program works for
# will simply end in "é", i.e we don't add an "e" for feminine subjects or an "s" for plural subjects. Here's an example with the verb "manger" (eating):
# J'ai mangé, tu as mangé, il a mangé, elle a mangé, nous avons mangé, vous avez mangé, ils ont mangé, elles ont mangé.
# Notice how the only thing changing was the auxiliary based on the subject and not the actual verb. These auxiliaries ('ai, as, a, a, avons, avez, ont, ont) are always the same when we use "avoir" and correspond to their respective subject
# Things get more complicated with irregular verbs which use auxiliary "être". Feminine verbs require an "e" and plural verbs require an "s". Let's take the verb "passer" (passing by) for example:
# Je suis passé(e), tu es passé(e), il est passé, elle est passée, nous sommes passé(e)s, vous êtes passé(e)s, ils sont passés, elles sont passées.
# Again, the auxliliaries (suis, es, est, est, sommes, êtes, sont, sont) for the "être" auxiliary are consistent with their respective subjects. What changes are the ending of the verbs.
# Since I am a girl, I would say "je suis passée" but if you are a boy, it would be "je suis passé". Same goes for subjects tu, nous and vous. They may or may not be feminine and may or may not have an extra "e".
# Hopefully that made sense. Now for the program. It defines a list of irregular verbs (if you know french, there are more, but again I'm focusing on the very standard ones). It also defines a list of subjects.
# It also containts a list of the auxiliaries and what they are with respect to their subject. The index of each auxiliary variation matches the index of its corresponding subject, for both auxiliaries.
# Based on the user's subject and verb input, the program checks if the verb is irregular and will output the subject, appropiate auxiliary and appropriate verb ending in a concatinated string
# A short explanation will also print based off the user's input

def fixmyfrench(x,y): # defining the function. x is the subject (je,tu,il,elle,nous,vous,ils,elles) and y is the verb without conjuagtion (must be entered like this to check if it's irregular)
    irregular=['rentrer','retourner','passer','arriver','entrer','tomber','rester','aller','monter'] # list of irregular verbs to check for 
    subjects=['je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles'] # list of subjects, will be used to check which one was inputted by the user and match that index with the appropriate auxiliary
    etre=['suis','es','est','est','sommes','êtes','sont','sont'] # list of "être" auxiliaries which are in order and correspond to their respective subject
    avoir=["j'ai",'as','a','a','avons','avez','ont','ont'] # list of "avoir" auxiliaries which are in order and correspond to their respective subject
    term_etre=['é','é','é','ée','és','és','és','ées'] # verb endings for when auxiliary "être" was used. These are in order with the subjects as well (indexes match)
    term_etre_fem=['ée','ée','é','ée','ées','ées','és','ées'] # verb endings for when auxiliary "être" was used and the subject is feminine. Indexes also match those of their subject
    term_avoir='é' # verb ending for auxiliary "avoir". super easy 
    fin=[] # initiating our final answer which will contain the subject, auxiliary and verb ending
    if y in irregular: # check if the user inputted an irregular verb, if so take the following steps
        for i in range(len(subjects)): # iterate over the subject indexes
            if subjects[i]==x and z=='feminine': # find index i where subject x is located. index i will be the same in our other lists so i is very important. This is the feminine case for irregular verbs.
                fin.append(subjects[i]) # append the subject
                fin.append(etre[i]) # append the auxiliary which corresponds to the subject
                fin.append(term_etre_fem[i]) # append the appropriate verb ending which corresponds to the subject and the auxiliary
            elif subjects[i]==x and z=='masculine': # if the subject was not feminine, jump here and find index i in subjects which is = to x. z will be masculine
                fin.append(subjects[i]) # append the subject
                fin.append(etre[i]) # append the auxiliary which corresponds to the subject
                fin.append(term_etre[i]) # append the verb ending that corresponds to the subject and the auxiliary
                
    else: # if the inputted verb y is not in irregular it will use auxiliary "avoir", do the following
        for i in range(len(subjects)): # iterate over the subject indexes
            if subjects[i]==x and x=='je': # find index i where subject x is located. This is the case where the subject is "Je", because we use "j'ai" as the subject and auxiliary.
                # since this is slightly different than for the other subjects, I put "j'ai" in the avoir list and will append this instead of j' and ai seperately. No rhyme or reason just what I chose
                fin.append(avoir[0]) # append "j'ai" if the subject is "je" and if the auxiliary is "avoir" 
                fin.append(term_avoir) # append the appropriate verb ending for the subject "je"
            elif subjects[i]==x: # find index i where subject x is located (program will jump to this if previous condition is not met i.e if the subject is not "je")
                fin.append(subjects[i]) # append the subject
                fin.append(avoir[i]) # append the appropriate auxiliary for the subject that was inputted
                fin.append(term_avoir) # append the verb ending

    return fin # list of the form [subject, auxiliary, verb ending] is the output
                

if __name__=="__main__": # initiating/calling the function
    irregular=['rentrer','retourner','passer','arriver','entrer','tomber','rester','aller','monter'] # same list of irregular verbs. will need this in a few steps
    etre=['suis','es','est','est','sommes','êtes','sont','sont'] # same list of "être" auxiliaries. will need this in a few steps
    x=str(input('enter your subject (je,tu,il/elle,nous,vous,ils/elles): ')) # user input for the subject
    y=str(input("enter your verb with no conjugation (à l'infinitif): ")) # user input for the non conjugated verb
    if x=='il' or x=='ils': # if x is il or ils, it's automatically masculine
        z='masculine'
    elif x=='elle' or x=='elles': # if x is elle or elles, it's automatically feminine
        z='feminine'
    else: # if x is not il, ils, elle or elles, we need the user to specify 
        z=str(input('is your subject feminine or masculine?: '))

    m=fixmyfrench(x,y) # call the function
    if x=='je' and y not in irregular: # case when the subject/auxilary is "j'ai". the indexes of the functions outputted list are slightly different
        print(m[0] +' '+'___'+m[1]) # print a concatinated string "j'ai ___(verb ending)"
    else: # for any other case, the output list m will have 3 indexes to concatinate 
        print(m[0]+' '+m[1]+' ' +'___'+m[2]) # print the concatinated string "subject auxiliary ___(verb ending)"
    if bool(m[1] in etre) == True: # if the auxiliary of our output is a form of the "être" auxiliary, it is an irregular verb, thus do the following:
        print('you entered an irregular verb. In this case, if the verb is feminine we add an "e" and if it is plural we add an "s" since we use auxiliary "être"')
    elif bool(m[1] in etre)==False: # if the auxiliary of our output is not a form of the "être" auxiliary, it is a regular verb, thus do the following:
        print('you entered a regular verb which uses auxiliary "avoir". In this case verbs will end in "é"') 
    

