#Final Project PROG1700
#Author: Rayn Brown W0491090
#Date: Dec. 1, 2023 
#Nova Scotia Sea Level Rise
#This program reads output from the NS Sea Level Rise Projections (CMIP5) dataset
#(Available: https://data.novascotia.ca/Nature-and-Environment/NS-Sea-Level-Rise-Projections-CMIP5-/t5sw-u3sr)
#and outputs a selection from this data set based on user requests.

#READY FOR MARKING

#import csv to read/write csv files
#import final_modules containing created functions for this program
import csv, final_modules

def main():

    #initialize variable used to exit the program
    program_exit = ""    #string to ask user if they want to contine or exit the program
    #while the program_exit variable is not [done], repeat program
    while program_exit.lower() != "done":  
        
        #initialize variables and lists
        source_list = []   #2d list of source data
        region_input = ""   #string of input from user selecting where they want the province-wide data or county-specific data
        region_list = []   #list of selected region(s) used to check which row(s) of the csv data to select from
        #list of all counties in Nova Scotia
        county_list = ["Annapolis","Antigonish","Cape Breton","Colchester","Cumberland","Digby","Guysborough","Halifax","Hants","Inverness","Kings","Lunenburg","Pictou","Queens","Richmond","Shelburne","Victoria","Yarmouth"]
        county = ""   #container of county name while asking user for which county/counties they want to select data for, is equal to "done" when user is done entering in county names
        year_input = ""   #string of input from user selecting where which year(s) they want data from
        year_list = []   #list of selected year(s) used to check which column(s) of the csv data to select from
        model_input = ""   #string of input from user selecting which model(s) they want data from
        model_list = []   #list of selected model(s) used to check whhich column(s) of the csv data to select from
        percentile_input = ""   #string of input from user selecting which percentile(s) they want data from
        percentile_list = []   #list of selected percentile(s) used to check which column(s) of the csv data to select from
        value_input = ""   #string of input from user selecting which value(s) they want data from
        value_list = []   #list of selected value(s) used to check which row(s) of the csv data to select from
        row_num = 0   #index of row number for accessing 2d source_list data
        new_row_list = []   #list of row to add to list of selected data
        selected_rows = []   #2d list of all data from selected row(s) of the source data 
        column_header = ""   #string of contructed column header from user inputs
        column_list = []   #list of column headers to select from selected_rows list
        selected_columns = [0,1]   #list of column indicies selected by user input, label columns 0 and 1 included in all selections
        new_row_string = ""   #string used to store selected data to append to a 2d list of selected data
        selected_data = []   #2d list of selected data
        repeat_county = False   #boolean flag to determine if inout was already typed in
        year_repeat = False   #boolean flag to determine if inout was already typed in
        percentile_repeat = False   #boolean flag to determine if inout was already typed in
        value_repeat = False   #boolean flag to determine if inout was already typed in
        valid_region_list = ["province","counties"]   #list of valid regions to select
        valid_region = False   #boolean flag to determine if valid region was inputted
        #list of valid county inputs
        valid_county_list = ["all","done","Annapolis","Antigonish","Cape Breton","Colchester","Cumberland","Digby","Guysborough","Halifax","Hants","Inverness","Kings","Lunenburg","Pictou","Queens","Richmond","Shelburne","Victoria","Yarmouth"]
        valid_county = False   #boolean flag to determine if valid county was inputted
        valid_year = False   #boolean flag to determine if valid year was inputted
        valid_year_list = ["all","done","2010","2045","2065","2095"]   #list of valid year inputs
        valid_model = False   #boolean flag to determine if valid model was inputted
        valid_model_list = ["low","high","both"]   #list of valid model inputs
        valid_percentile = False   #boolean flag to determine if valid percentile
        valid_perc_list = ["p05","p50","p95","done","all"]   #list of valid percentile inputs
        valid_value = False   #boolean flag used to determine if valid value inputted
        valid_value_list = ["slr_min","slr_mean","slr_max","all","done"]   #list of valid value inputs
        save_flag = False   #boolean flage used to determine if user wants to save results to a file

        #read data from csv file
        try:
            source_name = "NS_Sea_Level_Rise_Projections__CMIP5__20231201.csv"
            source_access = "r"

            with open(source_name, source_access) as source_handle:
                source_data = csv.reader(source_handle)
                for row in source_data:
                    source_list.append(row)
        
            #print title banner
            print("*" * 100)
            title = "NOVA SCOTIA SEA LEVEL RISE DATABASE"
            title_centre = title.center(100)
            print(title_centre)
            subtitle = "cm sea level rise projections from RCP4.5 and RCP8.5 scenariors"
            subtitle_centre =subtitle.center(100)
            print(subtitle_centre)
            print("*" * 100)

            #print instructions to user
            print("")
            introduction = "This program allows users to select data from NS Sea Level Rise Projections (CMIP5) database. The data supplied is minimum, mean, and maximum projected sea level rise in 2010, 2045, and 2065 for both RCP4.5 low emission scenario and RCP8.5 high emission scenario. Data is listed for Nova Scotia in general or each county, and in 5th, 50th (median), and 95th percentile." 
            into_wrapped = final_modules.wrappingtext(introduction)
            print(into_wrapped)
            instructions = "User will select whether they want the province-wide data or county-specific data or list of counties-specific data, which year(s) data, which model (RCP4.5 and/or RCP8.5), which percentile(s), and which values (minimum, mean, and maximum sea level rise)."
            instr_wrapped = final_modules.wrappingtext(instructions)
            print(instr_wrapped)
    
            #ask user for desired data parameters
            #ask if they want the province-wide data, or a list of provinces (and which provinces), or single province
            ask_region = "Do you want data for province-wide data or county-specific data for one or more counties? Type [province] for province-wide data and [counties] for county-specific data."
            region_wrapped = final_modules.wrappingtext(ask_region)
            print(region_wrapped)
            while valid_region == False:
                region_input = input("\nPlease input [province] or [counties]: ")
                #if input is "province", append "Nova Scotia" to list of selected regions (and only "Nova Scotia") 
                valid_region = final_modules.check_if_correct(region_input, valid_region_list)
                if valid_region == False:
                    print("\nWrong selection, please type [province] or [counties].")
            if valid_region == True:
                if region_input.lower() == "province":
                    region_list.append("Nova Scotia")
                #else if input is "counties", ask user for which counties they want
                elif region_input.lower() == "counties":
                #if user inputs "done" as county, stop asking for county names
                    #list availabe counties
                    print("\nAvailable provinces:")
                    for row in county_list:
                        print(f"\t{row}")
                    while county.lower() != "done":
                        while valid_county == False:
                            county = input("\nWhich county do you want to select for (type [all] to select all counties, [done] to finish, province name is case sensitive): ")
                            valid_county = final_modules.check_if_correct(county, valid_county_list)
                            if valid_county == False:
                                print("Wrong selection, please type one of the following county names:")
                                print("\nAvailable provinces:")
                                for row in county_list:
                                    print(f"\t{row}")
                        if county.lower() != "done":
                        #if input is "all", take all rows of county_list and add them to region_list
                            if county.lower() == "all":
                                for row in county_list:
                                    region_list.append(row)
                                #set county to "done", as all counties have been added
                                county = "done"
                            else:
                                repeat_county = final_modules.check_if_repeat(county, region_list)
                                if repeat_county == True:
                                    print("\nCounty has already been selected, please type in another county or [done].")
                                else:
                                    region_list.append(county)
                                repeat_county == False
                        else:
                            if len(region_list) < 1:
                                print("\nYou haven't selected a county yet, please selecte at least one county before typing [done].")
                                county = ""
                        valid_county = False
            
            #ask which year(s) the user wants data for
            print()
            ask_year = "Which year(s) do you want data for? The sea level rise projections have been calculated for 2010, 2045, 2065, and 2095."
            year_wrapped = final_modules.wrappingtext(ask_year)
            print(year_wrapped)
            while year_input != "done":
                while valid_year == False:
                    year_input = str(input("\nPlease input year(s) (type 2010, 2045, 2065, 2095, or [all] fo all; type [done] to finish): "))
                    valid_year = final_modules.check_if_correct(year_input, valid_year_list)
                    if valid_year == False:
                        print("\nWrong selection, please type [2010], [2045], [2065], [2095], [all], or [done].")
                if year_input.lower() != "done":
                    if year_input.lower() == "all":
                        year_list = ["2010","2045","2065","2095"]
                        year_input = "done"
                    else:
                        year_repeat = final_modules.check_if_repeat(year_input, year_list)
                        if year_repeat == True:
                            print("\nYear has already been selected, please type in another year or [done].")
                        else:
                            year_list.append(str(year_input))
                        year_repeat == False
                else:
                    if len(year_list) < 1:
                        print("\nYou haven't selected a year yet, please select at least one year before typing [done].")
                        year_input = ""
                valid_year = False

            #ask which model(s) the user wants data for
            print()
            ask_model = "Which model(s) do you want data for? The sea level rise projections have been calculated using the low emissions projection (RCP4.5) and the high emissions projection (RCP8.5)."
            model_wrapped = final_modules.wrappingtext(ask_model)
            print(model_wrapped)
            while valid_model == False:
                model_input = input("\nPlease input model (type [low], [high], or [both]): ")
                valid_model = final_modules.check_if_correct(model_input, valid_model_list)
                if valid_model == False:
                    print("\nWrong selection, please type [low] or [high] or [both].")
            if model_input.lower() == "low":
                model_list.append("rcp45")
            elif model_input.lower() == "high":
                model_list.append("rcp85")
            elif model_input.lower() == "both":
                model_list.append("rcp45")
                model_list.append("rcp85")

            #ask which percentile(s) the user wants data for
            print()
            ask_percentile = "What percentile(s) do you want data for? The 5th percentile is the value greater than of the lowest 5 percent of modelled calculations. The 50th percentile is the median value of the modelled calculations. The 95th Percentile is the value greater than the lowest 95 percent of the modelled calculations (or the value lower than the greates 5 percent of the modelled calculations)."
            perc_wrapped = final_modules.wrappingtext(ask_percentile)
            print(perc_wrapped)
            while percentile_input.lower() != "done":
                while valid_percentile == False:
                    percentile_input = input("\nPlease input percentile(s) (type [p05], [p50], [p95], or [all]; type [done] to finish): ")
                    valid_percentile = final_modules.check_if_correct(percentile_input, valid_perc_list)
                    if valid_percentile == False:
                        print("\nWrong selection, please type [p05], [p50], [p95], [all], or [done].")
                    if percentile_input.lower() != "done":
                        if percentile_input.lower() == "all":
                            percentile_list = ["p05","p50","p95"]
                            percentile_input = "done"
                        else:
                            percentile_repeat = final_modules.check_if_repeat(percentile_input, percentile_list)
                            if percentile_repeat == True:
                                print("\nPercentile has already been chosen. Please type in another percentile or [done].")
                            else:
                                percentile_list.append(percentile_input)
                        percentile_repeat == False
                    else:
                        if len(percentile_list) < 1:
                            print("\nYou haven't selected a percentile yet, please select at least one percentile before typing [done].")
                            percentile_input = ""
                valid_percentile = False

            #ask if they want minimum and/or mean and/or maximum values
            ask_value = "What values (minimum, mean, maximum) do you want data for?"
            value_wrapped = final_modules.wrappingtext(ask_value)
            print(value_wrapped)
            while value_input.lower() != "done":
                while valid_value == False:
                    value_input = input("\nPlease input value(s) (type [slr_min], [slr_mean], [slr_max], or [all] for all; type [done] to finish): ")
                    valid_value = final_modules.check_if_correct(value_input, valid_value_list)
                    if valid_value == False:
                        print("\nWrong selection, type [slr_min], [slr_mean], [slr_max], [all], or [done].") 
                    if value_input.lower() != "done":
                        if value_input.lower() == "all":
                            value_list = ["slr_max","slr_mean","slr_min"]
                            value_input = "done"
                        else:
                            value_repeat = final_modules.check_if_repeat(value_input, value_list)
                            if value_repeat == True:
                                print("\nValue has already be chosen. Please type in another value or [done].")
                            else:
                                value_list.append(value_input)
                            value_repeat == False
                    else:
                        if len(value_list) < 1:
                            print("\nYou haven't selected a value yet, please select at least one value before typing [done].")
                            value_input = ""
                valid_value = False

            #determin which rows and columns to select based on given user inputs on region, year(s), model(s), percentile(s), and values
            #add row 0 of source_list to selected_rows list (headers of the data)
            selected_rows.append(source_list[0])
            #check each row if it matches the selected inputs
            for row in source_list:
                #for each row in the region list, check row in source data
                for region_row in region_list:
                    #column 0 in source_data is the county name
                    #if column 0 in given row is equal to the region list value
                    if source_list[row_num][0] == region_row:
                        #for each rown in value list, check row in source data
                        for value_row in value_list:
                            #column 1 in source_data is the value (max/mean/min) of sea level rise
                            #if column 1 in given row is equal to the value list value 
                            if source_list[row_num][1] == value_row:
                                new_row_list = source_list[row_num]
                                #append selected row to list of selected data
                                selected_rows.append(new_row_list)
                row_num += 1

            #check each column if it matches the selected inputs
            #create string(s) of column header(s) to select data, and store them in a list
            for model in model_list:
                for percentile in percentile_list:
                    for year in year_list:
                        column_header = model + " " + percentile + " " + year
                        column_list.append(column_header)

            #check if each column matches the selected inputs
            header_row = selected_rows[0]
            for index in range(len(header_row)):
                for header in column_list:
                    if selected_rows[0][index] == header:
                        selected_columns.append(index)

            #use list of selected rows and list of selected columns to create 2d list of selected data
            #check for each row in selected_rows list
            row_num = 0
            for row in selected_rows:
                #check each value in index in row
                for index in range(len(selected_rows[0])):
                #check for each idex number in selected_columns list
                    for column in selected_columns:
                        if index == column:
                            if index == 0:
                                new_row_string += f"{selected_rows[row_num][index]}"
                            else:
                                new_row_string += f", {selected_rows[row_num][index]}"
                selected_data.append(new_row_string)
                row_num +=1
                new_row_string = ""

            #print selected data to the screen
            #get length and width of the selected_date table
            print()
            print("*" * 100)
            title = "RESULTS"
            title_centre = title.center(100)
            print(title_centre)
            subtitle = "cm sea level rise projections, selected by user"
            subtitle_centre =subtitle.center(100)
            print(subtitle_centre)
            print("*" * 100)
            print()
            for row in selected_data:
                replace_row = row.replace(",", "\t")
                print(replace_row)


            #ask user if they want to save the output to a csv file
            print("\nWould you like to save the results to a .csv file?")
            save_confirmation = input("Type [yes] to save: ")

            if save_confirmation.lower() == "yes":
                #write 2d list of selected data to a csv file
                while save_flag == False:
                    try:
                        file_name = str(input("\nWhat would you like to name the file (do not include file extension): "))
                        result_name = file_name + ".csv"
                        result_access = "w"

                        with open(result_name, result_access) as result_handle:
                            for row in selected_data:
                                result_handle.write(f"{row}\n")
                        save_flag = True
                        print(f"File saved as: {file_name}.csv")
                    except OSError:
                        print("OSError, file name was invalid.")
                    except PermissionError:
                        print("PermissionError, could not write file in that location.")
                    except FileNotFoundError:
                        print("FileNotFoundError, could not locate the directory.")
        except OSError:
            print("OSError, file could not be found.")
        except PermissionError:
            print("PermissionError, could not read file in that location.")
        except FileNotFoundError:
            print("FileNotFoundError, could not locate the directory.")
        #ask user if they wish to repeat the program or exit
        print("\nProgram complete, would you like to make another data selection?")
        program_exit = input("Type [done] to exit the program, type anything else to repeat: ")

if __name__ == "__main__":
    main()