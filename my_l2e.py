resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3},
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_record = []

def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None
print(find_resource("R002"))
print(find_resource("R999"))