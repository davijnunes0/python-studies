def main():
    
    spacecraft = {"name" : "James Webb Space Telescope","distance": 163}
    spacecraft["distance"] = 0.01
    
    print(create_report(spacecraft))

def create_report(spacecraft) -> str:
    return f"""
    ====== REPORT ======
     Name: {spacecraft["name"]}
     Distance: {spacecraft.get("distance","Unknown")} AU
     Year: {spacecraft.get("year","Unknown")}
    ====================
    """

if __name__ == "__main__":
    main()
