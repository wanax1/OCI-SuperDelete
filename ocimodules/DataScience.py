import oci
import time

WaitRefresh = 15


##############################################
# DeleteNotebooks
##############################################
def DeleteNotebooks(config, Compartments):
    AllItems = []
    object = oci.data_science.DataScienceClient(config)

    print("Getting all Notebook sessions")
    for Compartment in Compartments:
        try:
            items = oci.pagination.list_call_get_all_results(object.list_notebook_sessions, compartment_id=Compartment.id).data
            for item in items:
                if (item.lifecycle_state != "DELETED"):
                    AllItems.append(item)
                    print("- {} - {}".format(item.display_name, item.lifecycle_state))
            itemsPresent = True
        except Exception:
            print("Error getting all notebooks, likely service does not exist in this Region")
            itemsPresent = False

    while itemsPresent:
        count = 0
        for item in AllItems:
            try:
                itemstatus = object.get_notebook_session(notebook_session_id=item.id).data
                if itemstatus.lifecycle_state != "DELETED":
                    if itemstatus.lifecycle_state != "DELETING":
                        try:
                            print("Deleting: {}".format(itemstatus.display_name))
                            object.delete_notebook_session(notebook_session_id=itemstatus.id)
                        except Exception:
                            print("error trying to delete: {}".format(itemstatus.display_name))
                    else:
                        print("{} = {}".format(itemstatus.display_name, itemstatus.lifecycle_state))
                    count = count + 1
            except Exception:
                print("-----------------> error deleting {}, probably already deleted: {}".format(item.display_name, item.lifecycle_state))
        if count > 0:
            print("Waiting for all Objects to be deleted...")
            time.sleep(WaitRefresh)
        else:
            itemsPresent = False
    print("All Notebook Objects deleted!")


##############################################
# DeleteModels
##############################################
def DeleteModels(config, Compartments):
    AllItems = []
    object = oci.data_science.DataScienceClient(config)

    print("Getting all Data Science Models")
    for Compartment in Compartments:
        try:
            items = oci.pagination.list_call_get_all_results(object.list_models, compartment_id=Compartment.id).data
            for item in items:
                if (item.lifecycle_state != "DELETED"):
                    AllItems.append(item)
                    print("- {} - {}".format(item.display_name, item.lifecycle_state))
            itemsPresent = True
        except Exception:
            print("Error getting all Data Science Models, likely service does not exist in this Region")
            itemsPresent = False

    while itemsPresent:
        count = 0
        for item in AllItems:
            try:
                itemstatus = object.get_model(model_id=item.id).data
                if itemstatus.lifecycle_state != "DELETED":
                    if itemstatus.lifecycle_state != "DELETING":
                        try:
                            print("Deleting: {}".format(itemstatus.display_name))
                            object.delete_model(model_id=itemstatus.id)
                        except Exception:
                            print("error trying to delete: {}".format(itemstatus.display_name))
                    else:
                        print("{} = {}".format(itemstatus.display_name, itemstatus.lifecycle_state))
                    count = count + 1
            except Exception:
                print("-----------------> error deleting {}, probably already deleted: {}".format(item.display_name, item.lifecycle_state))
        if count > 0:
            print("Waiting for all Objects to be deleted...")
            time.sleep(WaitRefresh)
        else:
            itemsPresent = False
    print("All Data Science Models Objects deleted!")


##############################################
# DeleteModelDeployments
##############################################
def DeleteModelDeployments(config, Compartments):
    AllItems = []
    object = oci.data_science.DataScienceClient(config)

    print("Getting all Data Science Models")
    for Compartment in Compartments:
        try:
            items = oci.pagination.list_call_get_all_results(object.list_model_deployments, compartment_id=Compartment.id).data
            for item in items:
                if (item.lifecycle_state != "DELETED"):
                    AllItems.append(item)
                    print("- {} - {}".format(item.display_name, item.lifecycle_state))
            itemsPresent = True
        except Exception:
            print("Error getting all Data Science model deployments, likely service does not exist in this Region")
            itemsPresent = False

    while itemsPresent:
        count = 0
        for item in AllItems:
            try:
                itemstatus = object.get_model_deployment(model_deployment_id=item.id).data
                if itemstatus.lifecycle_state != "DELETED":
                    if itemstatus.lifecycle_state != "DELETING":
                        try:
                            print("Deleting: {}".format(itemstatus.display_name))
                            object.delete_model_deployment(model_deployment_id=itemstatus.id)
                        except Exception:
                            print("error trying to delete: {}".format(itemstatus.display_name))
                    else:
                        print("{} = {}".format(itemstatus.display_name, itemstatus.lifecycle_state))
                    count = count + 1
            except Exception:
                print("-----------------> error deleting {}, probably already deleted: {}".format(item.display_name, item.lifecycle_state))
        if count > 0:
            print("Waiting for all Objects to be deleted...")
            time.sleep(WaitRefresh)
        else:
            itemsPresent = False
    print("All Data Science Models Objects deleted!")


##############################################
# DeleteProjects
##############################################
def DeleteProjects(config, Compartments):
    AllItems = []
    object = oci.data_science.DataScienceClient(config)

    print("Getting all DataScience Projects")
    for Compartment in Compartments:
        try:
            items = oci.pagination.list_call_get_all_results(object.list_projects,
                                                             compartment_id=Compartment.id).data
            for item in items:
                if (item.lifecycle_state != "DELETED"):
                    AllItems.append(item)
                    print("- {} - {}".format(item.display_name, item.lifecycle_state))
            itemsPresent = True
        except Exception:
            print("Error getting all notebooks, likely service does not exist in this Region")
            itemsPresent = False

    while itemsPresent:
        count = 0
        for item in AllItems:
            try:
                itemstatus = object.get_project(project_id=item.id).data
                if itemstatus.lifecycle_state != "DELETED":
                    if itemstatus.lifecycle_state != "DELETING":
                        try:
                            print("Deleting: {}".format(itemstatus.display_name))
                            object.delete_project(project_id=itemstatus.id)
                        except Exception:
                            print("error trying to delete: {}".format(itemstatus.display_name))
                    else:
                        print("{} = {}".format(itemstatus.display_name, itemstatus.lifecycle_state))
                    count = count + 1
            except Exception:

                print("-----------------> error deleting {}, probably already deleted: {}".format(item.display_name, item.lifecycle_state))
        if count > 0:
            print("Waiting for all Objects to be deleted...")
            time.sleep(WaitRefresh)
        else:
            itemsPresent = False
    print("All DataScience Projects Objects deleted!")
