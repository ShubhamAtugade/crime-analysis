import random
import time
import json
from datetime import datetime

# City, State, and Police Station mapping with coordinates
city_state_police_map = {
    'Andhra Pradesh': {
        'state': 'Andhra Pradesh',
        'cities': {
            'Visakhapatnam': {
                'police_stations': ['City Police Station', 'Madhurawada Police Station'],
                'coordinates': {'lat': 17.6869, 'lon': 83.2185}
            },
            'Vijayawada': {
                'police_stations': ['One Town Police Station', 'Gollapudi Police Station'],
                'coordinates': {'lat': 16.5063, 'lon': 80.6480}
            },
            'Guntur': {
                'police_stations': ['Guntur Urban Police Station', 'Chilakaluripet Police Station'],
                'coordinates': {'lat': 16.3067, 'lon': 80.4545}
            },
            'Tirupati': {
                'police_stations': ['Tirupati Urban Police Station', 'Chandragiri Police Station'],
                'coordinates': {'lat': 13.6288, 'lon': 79.4197}
            }
        }
    },
    
    'Arunachal Pradesh': {
        'state': 'Arunachal Pradesh',
        'cities': {
            'Itanagar': {
                'police_stations': ['Itanagar Police Station', 'Naharlagun Police Station'],
                'coordinates': {'lat': 27.1000, 'lon': 93.6167}
        },
            'Tawang': {
                'police_stations': ['Tawang Police Station', 'Jang Police Station'],
                'coordinates': {'lat': 27.5578, 'lon': 91.9863}
            }
        }
    },
    
    'Assam': {
        'state': 'Assam',
        'cities': {
            'Guwahati': {
                'police_stations': ['Dispur Police Station', 'Guwahati Railway Police Station'],
                'coordinates': {'lat': 26.1445, 'lon': 91.7362}
            },
            'Dibrugarh': {
                'police_stations': ['Dibrugarh Police Station', 'Duliajan Police Station'],
                'coordinates': {'lat': 27.4790, 'lon': 94.9111}
            }
        }
    },
    
    'Bihar': {
        'state': 'Bihar',
        'cities': {
            'Patna': {
                'police_stations': ['Patna City Police Station', 'Patna Railway Police Station'],
                'coordinates': {'lat': 25.5941, 'lon': 85.1376}
            },
            'Gaya': {
                'police_stations': ['Gaya Police Station', 'Makhdumpur Police Station'],
                'coordinates': {'lat': 24.7959, 'lon': 85.0263}
            },
            'Bhagalpur': {
                'police_stations': ['Bhagalpur Police Station', 'Naugachhia Police Station'],
                'coordinates': {'lat': 25.2470, 'lon': 87.0053}
            },
            'Muzzafarpur': {
                'police_stations': ['Muzaffarpur Police Station', 'Muzaffarpur Women Police Station'],
                'coordinates': {'lat': 26.1200, 'lon': 85.3742}
            }
        }
    },
    
    'Chhattisgarh': {
        'state': 'Chhattisgarh',
        'cities': {
            'Raipur': {
                'police_stations': ['Raipur Police Station', 'Raipur Traffic Police Station'],
                'coordinates': {'lat': 21.2514, 'lon': 81.6296}
            },
            'Bilaspur': {
                'police_stations': ['Bilaspur Police Station', 'Bilaspur Railway Police Station'],
                'coordinates': {'lat': 22.0798, 'lon': 82.1444}
            },
            'Korba': {
                'police_stations': ['Korba Police Station', 'Korba West Police Station'],
                'coordinates': {'lat': 22.3581, 'lon': 82.7024}
            }
        }
    },

    'Delhi': {
        'state': 'Delhi',
        'cities': {
            'North Delhi': {
                'police_stations': ['North Delhi Police Station', 'Civil Lines Police Station'],
                'coordinates': {'lat': 28.7041, 'lon': 77.1025}
            },
            'South Delhi': {
                'police_stations': ['South Delhi Police Station', 'Kalkaji Police Station'],
                'coordinates': {'lat': 28.5494, 'lon': 77.2500}
            },
            'West Delhi': {
                'police_stations': ['West Delhi Police Station', 'Janakpuri Police Station'],
                'coordinates': {'lat': 28.6352, 'lon': 77.0929}
            },
            'East Delhi': {
                'police_stations': ['East Delhi Police Station', 'Preet Vihar Police Station'],
                'coordinates': {'lat': 28.6519, 'lon': 77.2312}
            }
        }
    },

    'Goa': {
        'state': 'Goa',
        'cities': {
            'Panaji': {
                'police_stations': ['Panaji Police Station', 'Old Goa Police Station'],
                'coordinates': {'lat': 15.4909, 'lon': 73.8278}
            },
            'Margao': {
                'police_stations': ['Margao Police Station', 'Fatorda Police Station'],
                'coordinates': {'lat': 15.2993, 'lon': 73.9336}
            }
        }
    },

    'Gujarat': {
        'state': 'Gujarat',
        'cities': {
            'Ahmedabad': {
                'police_stations': ['Ahmedabad Police Station', 'Ellisbridge Police Station', 'Naranpura Police Station', 'Maninagar Police Station'],
                'coordinates': {'lat': 23.0225, 'lon': 72.5714}
            },
            'Surat': {
                'police_stations': ['Surat Police Station', 'Varachha Police Station', 'Adajan Police Station', 'Udhna Police Station', 'Gopipura Police Station'],
                'coordinates': {'lat': 21.1702, 'lon': 72.8311}
            },
            'Vadodara': {
                'police_stations': ['Vadodara Police Station', 'Ajwa Police Station', 'Fatehgunj Police Station', 'Gotri Police Station'],
                'coordinates': {'lat': 22.3072, 'lon': 73.1812}
            },
            'Rajkot': {
                'police_stations': ['Rajkot Police Station', 'Gundala Police Station', 'Kalavad Police Station', 'Sadar Police Station', 'Mavdi Police Station'],
                'coordinates': {'lat': 22.3039, 'lon': 70.8022}
            },
            'Bhavnagar': {
                'police_stations': ['Bhavnagar Police Station', 'Sihor Police Station', 'Gadhada Police Station', 'Palitana Police Station'],
                'coordinates': {'lat': 21.7601, 'lon': 72.1500}
            },
            'Junagadh': {
                'police_stations': ['Junagadh Police Station', 'Upleta Police Station', 'Veraval Police Station', 'Mendarda Police Station'],
                'coordinates': {'lat': 21.5219, 'lon': 70.4625}
            },
            'Anand': {
                'police_stations': ['Anand Police Station', 'Petlad Police Station', 'Sojitra Police Station', 'Borsad Police Station'],
                'coordinates': {'lat': 22.5711, 'lon': 72.9622}
            },
            'Navsari': {
                'police_stations': ['Navsari Police Station', 'Gandevi Police Station', 'Chikhli Police Station', 'Vansda Police Station'],
                'coordinates': {'lat': 20.9625, 'lon': 72.9205}
            }
        }
    },

    'Haryana': {
        'state': 'Haryana',
        'cities': {
            'Chandigarh': {
                'police_stations': ['Chandigarh Sector 17 Police Station', 'Chandigarh Sector 31 Police Station'],
                'coordinates': {'lat': 30.7333, 'lon': 76.7794}
            },
            'Gurugram': {
                'police_stations': ['Gurugram Police Station', 'Cyber City Police Station'],
                'coordinates': {'lat': 28.4595, 'lon': 77.0266}
            },
            'Faridabad': {
                'police_stations': ['Faridabad Police Station', 'Sector 31 Police Station'],
                'coordinates': {'lat': 28.4089, 'lon': 77.3188}
            }
        }
    },

    'Himachal Pradesh': {
        'state': 'Himachal Pradesh',
        'cities': {
            'Shimla': {
                'police_stations': ['Shimla Police Station', 'Chhota Shimla Police Station'],
                'coordinates': {'lat': 31.1048, 'lon': 77.1734}
            },
            'Manali': {
                'police_stations': ['Manali Police Station', 'Naggar Police Station'],
                'coordinates': {'lat': 32.2396, 'lon': 77.1887}
            }
        }
    },

    'Jharkhand': {
        'state': 'Jharkhand',
        'cities': {
            'Ranchi': {
                'police_stations': ['Ranchi Police Station', 'Kotwali Police Station'],
                'coordinates': {'lat': 23.3441, 'lon': 85.3096}
            },
            'Jamshedpur': {
                'police_stations': ['Jamshedpur Police Station', 'Sakchi Police Station'],
                'coordinates': {'lat': 22.8046, 'lon': 86.2027}
            }
        }
    },
    
    'Karnataka': {
        'state': 'Karnataka',
        'cities': {
            'Bengaluru': {
                'police_stations': ['Bengaluru City Police Station', 'Ulsoor Police Station'],
                'coordinates': {'lat': 12.9716, 'lon': 77.5946}
            },
            'Mysuru': {
                'police_stations': ['Mysuru Police Station', 'Nazarbad Police Station'],
                'coordinates': {'lat': 12.2958, 'lon': 76.6394}
            },
            'Hubballi': {
                'police_stations': ['Hubballi Police Station', 'Keshwapur Police Station'],
                'coordinates': {'lat': 15.3647, 'lon': 75.1330}
            },
            'Mangaluru': {
                'police_stations': ['Mangaluru Police Station', 'Pandeshwar Police Station'],
                'coordinates': {'lat': 12.9141, 'lon': 74.8560}
            }
        }
    },

    'Kerala': {
        'state': 'Kerala',
        'cities': {
            'Thiruvananthapuram': {
                'police_stations': ['Thiruvananthapuram Police Station', 'Nanthancode Police Station'],
                'coordinates': {'lat': 8.5241, 'lon': 76.9366}
            },
            'Kochi': {
                'police_stations': ['Kochi Police Station', 'Marine Drive Police Station'],
                'coordinates': {'lat': 9.9312, 'lon': 76.2673}
            },
            'Kozhikode': {
                'police_stations': ['Kozhikode Police Station', 'Kozhikode East Police Station'],
                'coordinates': {'lat': 11.2588, 'lon': 75.7804}
            }
        }
    },
    
    'Madhya Pradesh': {
        'state': 'Madhya Pradesh',
        'cities': {
            'Bhopal': {
                'police_stations': ['Bhopal Police Station', 'Habibganj Police Station'],
                'coordinates': {'lat': 23.2599, 'lon': 77.4126}
            },
            'Indore': {
                'police_stations': ['Indore Police Station', 'Indore Railway Police Station'],
                'coordinates': {'lat': 22.7196, 'lon': 75.8577}
            },
            'Jabalpur': {
                'police_stations': ['Jabalpur Police Station', 'Madhotal Police Station'],
                'coordinates': {'lat': 23.1815, 'lon': 79.9555}
            },
            'Gwalior': {
                'police_stations': ['Gwalior Police Station', 'Civil Lines Police Station'],
                'coordinates': {'lat': 26.2183, 'lon': 78.1820}
            }
        }
    },
    
    'Maharashtra': {
        'state': 'Maharashtra',
        'cities': {
            'Mumbai': {
                'police_stations': ['Colaba Police Station', 'Marine Drive Police Station', 'Bandra Police Station', 'Andheri Police Station','Prabhadevi Police Station', 'Shivaji Park Police Station', 'Dadar Police Station'],
                'coordinates': {'lat': 19.0760, 'lon': 72.8777}
            },
            'Pune': {
                'police_stations': ['Shivajinagar Police Station','Kothrud Police Station', 'Hadapsar Police Station','Hinjawadi Police Station'],
                'coordinates': {'lat': 18.5204, 'lon': 73.8567}
            },
            'Nagpur': {
                'police_stations': ['Sitabuldi Police Station', 'Civil Lines Police Station','Laxmi Nagar Police Station'],
                'coordinates': {'lat': 21.1458, 'lon': 79.0882}
            },
            'Chhatrapati Sambhaji Nagar': {
                'police_stations': ['Chhatrapati Sambhaji Nagar Police Station', 'Paithan Police Station'],
                'coordinates': {'lat': 19.8762, 'lon': 75.3433}
            },
            'Nashik': {
                'police_stations': ['Nashik Road Police Station', 'Panchavati Police Station'],
                'coordinates': {'lat': 19.9975, 'lon': 73.7878}
            },
            'Kolhapur': {
                'police_stations': ['Kolhapur Police Station', 'Shivaji Park Police Station', 'Mahalaxmi Police Station', 'Gokul Shirgaon Police Station'],
                'coordinates': {'lat': 16.7057, 'lon': 74.2430}
            },
            'Thane Police Station': {
                'police_stations': ['Thane City Police Station','Airoli Police Station' 'Kalwa Police Station', 'Wagle Estate Police Station', 'Vartak Nagar Police Station', 'Dombivli Police Station','Mulund Police Station'],
                'coordinates': {'lat': 19.2183, 'lon': 72.9784}
            }
        }
    },
    
    'Manipur': {
        'state': 'Manipur',
        'cities': {
            'Imphal': {
                'police_stations': ['Imphal Police Station', 'Lamphel Police Station'],
                'coordinates': {'lat': 24.8178, 'lon': 93.9368}
            },
            'Churachandpur': {
                'police_stations': ['Churachandpur Police Station', 'Songjang Police Station'],
                'coordinates': {'lat': 24.3089, 'lon': 93.6154}
            }
        }
    },
    
    'Meghalaya': {
        'state': 'Meghalaya',
        'cities': {
            'Shillong': {
                'police_stations': ['Shillong Police Station', 'Mawlai Police Station'],
                'coordinates': {'lat': 25.5788, 'lon': 91.8933}
            },
            'Tura': {
                'police_stations': ['Tura Police Station', 'Rajabala Police Station'],
                'coordinates': {'lat': 25.5522, 'lon': 90.2177}
            }
        }
    },

    'Mizoram': {
        'state': 'Mizoram',
        'cities': {
            'Aizawl': {
                'police_stations': ['Aizawl Police Station', 'Durtlang Police Station'],
                'coordinates': {'lat': 23.7360, 'lon': 92.7176}
            },
            'Lunglei': {
                'police_stations': ['Lunglei Police Station', 'Tlabung Police Station'],
                'coordinates': {'lat': 23.1340, 'lon': 92.7376}
            }
        }
    },
    
    'Nagaland': {
        'state': 'Nagaland',
        'cities': {
            'Kohima': {
                'police_stations': ['Kohima Police Station', 'Thizama Police Station'],
                'coordinates': {'lat': 25.6723, 'lon': 94.1127}
            },
            'Dimapur': {
                'police_stations': ['Dimapur Police Station', 'Chumukedima Police Station'],
                'coordinates': {'lat': 25.9073, 'lon': 93.7194}
            }
        }
    },
    
    'Odisha': {
        'state': 'Odisha',
        'cities': {
            'Bhubaneswar': {
                'police_stations': ['Bhubaneswar Police Station', 'Saheed Nagar Police Station'],
                'coordinates': {'lat': 20.2961, 'lon': 85.8189}
            },
            'Cuttack': {
                'police_stations': ['Cuttack Police Station', 'Markat Nagar Police Station'],
                'coordinates': {'lat': 20.4625, 'lon': 85.8828}
            }
        }
    },
    
    'Punjab': {
        'state': 'Punjab',
        'cities': {
            'Chandigarh': {
                'police_stations': ['Chandigarh Police Station', 'Sector 17 Police Station'],
                'coordinates': {'lat': 30.7333, 'lon': 76.7794}
            },
            'Amritsar': {
                'police_stations': ['Amritsar Police Station', 'Civil Lines Police Station'],
                'coordinates': {'lat': 31.6340, 'lon': 74.8723}
            },
            'Ludhiana': {
                'police_stations': ['Ludhiana Police Station', 'Model Town Police Station'],
                'coordinates': {'lat': 30.9009, 'lon': 75.8573}
            },
            'Jalandhar': {
                'police_stations': ['Jalandhar Police Station', 'Civil Lines Police Station'],
                'coordinates': {'lat': 31.3254, 'lon': 75.5793}
            }
        }
    },
    
    'Rajasthan': {
        'state': 'Rajasthan',
        'cities': {
            'Jaipur': {
                'police_stations': ['Jaipur Police Station', 'Vaishali Nagar Police Station'],
                'coordinates': {'lat': 26.9124, 'lon': 75.7873}
            },
            'Udaipur': {
                'police_stations': ['Udaipur Police Station', 'Fatehpura Police Station'],
                'coordinates': {'lat': 24.5854, 'lon': 73.7125}
            },
            'Jodhpur': {
                'police_stations': ['Jodhpur Police Station', 'Ratanada Police Station'],
                'coordinates': {'lat': 26.2389, 'lon': 73.0248}
            },
            'Bikaner': {
                'police_stations': ['Bikaner Police Station', 'Civil Lines Police Station'],
                'coordinates': {'lat': 28.0229, 'lon': 73.3112}
            }
        }
    },
    
    'Sikkim': {
        'state': 'Sikkim',
        'cities': {
            'Gangtok': {
                'police_stations': ['Gangtok Police Station', 'Tadong Police Station'],
                'coordinates': {'lat': 27.3389, 'lon': 88.6070}
            },
            'Namchi': {
                'police_stations': ['Namchi Police Station', 'Melli Police Station'],
                'coordinates': {'lat': 27.0838, 'lon': 88.6072}
            }
        }
    },
    
    'Tamil Nadu': {
        'state': 'Tamil Nadu',
        'cities': {
            'Chennai': {
                'police_stations': ['Central Police Station', 'T Nagar Police Station'],
                'coordinates': {'lat': 13.0827, 'lon': 80.2707}
            },
            'Coimbatore': {
                'police_stations': ['Coimbatore North Police Station', 'R S Pudur Police Station'],
                'coordinates': {'lat': 11.0168, 'lon': 76.9558}
            },
            'Madurai': {
                'police_stations': ['Madurai South Police Station', 'Siddha Nagar Police Station'],
                'coordinates': {'lat': 9.9250, 'lon': 78.1193}
            },
            'Salem': {
                'police_stations': ['Salem Town Police Station', 'Mettur Police Station'],
                'coordinates': {'lat': 11.6643, 'lon': 78.1461}
            }
        }
    },
    
    'Telangana': {
        'state': 'Telangana',
        'cities': {
            'Hyderabad': {
                'police_stations': ['Hyderabad Police Station', 'Banjara Hills Police Station'],
                'coordinates': {'lat': 17.3850, 'lon': 78.4867}
            },
            'Warangal': {
                'police_stations': ['Warangal Police Station', 'Kazipet Police Station'],
                'coordinates': {'lat': 17.9784, 'lon': 79.5941}
            },
            'Khammam': {
                'police_stations': ['Khammam Police Station', 'Srinivasa Colony Police Station'],
                'coordinates': {'lat': 17.2477, 'lon': 80.1490}
            },
            'Nizamabad': {
                'police_stations': ['Nizamabad Police Station', 'Bodhan Police Station'],
                'coordinates': {'lat': 18.6713, 'lon': 78.0994}
            }
        }
    },
    
    'Tripura': {
        'state': 'Tripura',
        'cities': {
            'Agartala': {
                'police_stations': ['Agartala Police Station', 'Battala Police Station'],
                'coordinates': {'lat': 23.8315, 'lon': 91.2868}
            },
            'Udaipur': {
                'police_stations': ['Udaipur Police Station', 'Kumarghat Police Station'],
                'coordinates': {'lat': 23.2295, 'lon': 91.3072}
            }
        }
    },
    
    'Uttarakhand': {
        'state': 'Uttarakhand',
        'cities': {
            'Dehradun': {
                'police_stations': ['Dehradun Police Station', 'Raipur Police Station'],
                'coordinates': {'lat': 30.3165, 'lon': 78.0322}
            },
            'Haridwar': {
                'police_stations': ['Haridwar Police Station', 'Bhupatwala Police Station'],
                'coordinates': {'lat': 29.9457, 'lon': 78.1642}
            }
        }
    },
    
    'Uttar Pradesh': {
        'state': 'Uttar Pradesh',
        'cities': {
            'Lucknow': {
                'police_stations': ['Hazratganj Police Station', 'Alambagh Police Station'],
                'coordinates': {'lat': 26.8467, 'lon': 80.9462}
            },
            'Agra': {
                'police_stations': ['Agra City Police Station', 'Sadar Bazar Police Station'],
                'coordinates': {'lat': 27.1767, 'lon': 78.0081}
            },
            'Varanasi': {
                'police_stations': ['Varanasi Cantt Police Station', 'Lalpur Police Station'],
                'coordinates': {'lat': 25.3176, 'lon': 82.9739}
            },
            'Kanpur': {
                'police_stations': ['Kanpur Nagar Police Station', 'Panki Police Station'],
                'coordinates': {'lat': 26.4499, 'lon': 80.3319}
            }
        }
    },
    
    'West Bengal': {
        'state': 'West Bengal',
        'cities': {
            'Kolkata': {
                'police_stations': ['Kolkata Police Station', 'Park Street Police Station'],
                'coordinates': {'lat': 22.5726, 'lon': 88.3639}
            },
            'Howrah': {
                'police_stations': ['Howrah Police Station', 'Liluah Police Station'],
                'coordinates': {'lat': 22.5761, 'lon': 88.3184}
            },
            'Siliguri': {
                'police_stations': ['Siliguri Police Station', 'Pradhannagar Police Station'],
                'coordinates': {'lat': 26.7279, 'lon': 88.3953}
            },
            'Durgapur': {
                'police_stations': ['Durgapur Police Station', 'Benachity Police Station'],
                'coordinates': {'lat': 23.5257, 'lon': 87.3115}
            }
        }
    }, 
}

# Generate random crime data
def generate_random_data():
    state = random.choice(list(city_state_police_map.keys()))
    city = random.choice(list(city_state_police_map[state]['cities'].keys()))
    city_data = city_state_police_map[state]['cities'][city]

    entry = {
        'crime_id': f'CR-{random.randint(1000, 9999)}',
        'crime_type': random.choice(['Theft', 'Assault', 'Robbery', 'Fraud']),
        'members_involved': random.randint(1, 5),
        'crime_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'city': city,
        'state': state,
        'police_station': random.choice(city_data['police_stations']),
        'coordinates': city_data['coordinates']
    }
    return entry

# Function to append data every 2 seconds and refresh it every 20 seconds
def refresh_data():
    output_file = "data.json"
    
    # Check if the file exists, if not, create an empty list
    if not os.path.exists(output_file):
        with open(output_file, 'w') as f:
            json.dump([], f)

    try:
        while True:
            # Generate new crime data every 2 seconds
            new_data = generate_random_data()
            with open(output_file, 'r+') as f:
                existing_data = json.load(f)  # Load existing data
                existing_data.append(new_data)  # Append new data
                f.seek(0)  # Go to the beginning of the file
                json.dump(existing_data, f, indent=4)  # Save the updated data
            print(f"New data added to {output_file}")
            
            time.sleep(2)  # Wait for 2 seconds before adding the next entry

            # Refresh the data after 20 seconds (optional behavior if you want a reset/flush)
            if time.time() % 20 == 0:
                with open(output_file, 'r+') as f:
                    existing_data = json.load(f)
                    print(f"Refreshing data. Current records: {len(existing_data)}")
                    # You could add additional logic to refresh or adjust data here
                time.sleep(18)  # Wait 18 seconds before next refresh cycle to ensure every 20 seconds
    except KeyboardInterrupt:
        print("Data generation stopped.")

if __name__ == "__main__":
    import os
    refresh_data()