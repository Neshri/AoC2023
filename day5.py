
def get_destination(source, convert_map):
    destination = source
    for x in convert_map:
        if x[1] <= source < x[1] + x[2]:
            destination = x[0] + (source - x[1])
            break
    return destination

def get_destinations(source, s_range, convert_map):
    destinations = []
    for x in convert_map:
        # Check if overlap
        if not (source + s_range < x[1] or source > x[1] + x[2]):
            overlap_start = max(source, x[1])
            overlap_end = min(source + s_range, x[1] + x[2])
            # Convert
            destinations.append([overlap_start, overlap_end - overlap_start, x[0] + overlap_start - x[1]])
    destinations.sort()
    # Insert the unlisted mappings
    point = source
    missing = []
    for x in destinations:
        if x[0] > point:
            missing.append([point, x[0] - point, point])
        point = x[0] + x[1]
    if point < source + s_range:
        missing.append([point, source + s_range - point, point])
    destinations.extend(missing)
    # Reformat
    for i in range(len(destinations)):
        destinations[i] = [destinations[i][2], destinations[i][1]]
    return destinations

with open("day5input.txt") as f:
    data = [x.strip() for x in f.readlines()]
seeds = [int(x) for x in data[0].split(" ")[1:]]

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
map_list = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
maps = {"seed-to-soil map:": seed_to_soil, "soil-to-fertilizer map:": soil_to_fertilizer, "fertilizer-to-water map:": fertilizer_to_water, "water-to-light map:": water_to_light,
        "light-to-temperature map:": light_to_temperature, "temperature-to-humidity map:": temperature_to_humidity, "humidity-to-location map:": humidity_to_location}
current_map = seed_to_soil
for line in data[2:]:
    if line == "":
        continue
    if line in maps.keys():
        current_map.sort()
        current_map = maps[line]
        continue
    numbers = [int(x) for x in line.split(" ")]
    current_map.append(numbers)
humidity_to_location.sort()

seed_to_location = {}
for seed in seeds:
    destinations = get_destination(seed, seed_to_soil)
    for m in map_list[1:]:
        destinations = get_destination(destinations, m)
    seed_to_location[seed] = destinations

print("The first answer is:", min(seed_to_location.values()))

seed_to_location = {}
for i in range(0, len(seeds), 2):
    destinations = get_destinations(seeds[i], seeds[i+1], map_list[0])
    for m in map_list[1:]:
        new_destinations = []
        for d in destinations:
            new_destinations.extend(get_destinations(d[0], d[1], m))
        destinations = new_destinations
    seed_to_location[seeds[i]] = destinations
   
answer = float("inf")
for value in seed_to_location.values():
    for v in value:
        if v[0] < answer:
            answer = v[0]
print("The second answer is:", answer)
