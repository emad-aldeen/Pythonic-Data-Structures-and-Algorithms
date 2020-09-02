def multi_bracket_validation(input):
    '''
    it cheack your sentence if all brackets opend and closed well:
        inp ---> string
        out >> boleen with printed the reson if it fales..
    '''
    open_tag = ['[', '(', '{']
    close_tag = [']', ')', '}']
    complete_tag = ['[]', '()', '{}']


    inputs = list(input)
    x = []
    z = 0
    for i in range(len(inputs)):
        if inputs[i-z] in open_tag:
            x.append(inputs[i-z])
        if inputs[i-z] in close_tag:
            if len(x) > 0:
                if x[-1] + inputs[i-z] in complete_tag:
                    del inputs[i-z] 
                    del x[-1]
                    z += 1      
                else:
                    print(f'error closing {inputs[i-1]}, Doesn’t match opening {x[-1]}')
                    return False
            else:
                print(f'error closing {inputs[i-z]} arrived without corresponding opening!!')
    if len(x) > 0:
        print(f"error unmatched opening {','.join(x)} remaining")
        return False
    else:
        return True




if __name__ == '__main__':
    print(multi_bracket_validation('{ddd{[[fdslkflsndljf]]}}{{}}'))











    # print(inputs)
    # for i in range(len(inputs)):
    #     print(i)
    #     if inputs[i] in open_tag or inputs[i] in close_tag:
    #         print(i, inputs[i])
    #         for j in range(len(inputs[i:])):
    #             print(i, j, inputs[i])
    #             if inputs[i:][j] in close_tag:
    #                 print(i, j, inputs[i], inputs[i:][j])
    #                 if inputs[i] + inputs[i:][j] in complete_tag:
    #                     del inputs[i:][j]
    #                     del inputs[i]
    #                     for ii in range(len(inputs[i:])):
    #                         if inputs[i:][ii] in close_tag:
    #                             if x[-1] + inputs[i:][ii] in complete_tag:
    #                                 del inputs[i:][ii]
    #                                 del x[-1]
    #                                 continue
    #                             else:
    #                                 print(f'error closing {inputs[i:][ii]}, Doesn’t match opening {x[-1]}')
    #                                 return False 
    #                     break
    #                 else:
    #                     print(f'error closing {inputs[i:][j]}, Doesn’t match opening {inputs[i]}')
    #                     return False
    #             elif inputs[i:][j] in open_tag:
    #                 print(i, j, inputs[i] ,inputs[i:][j], 'appended!')
    #                 x.append(inputs[i])
    #                 break
                


