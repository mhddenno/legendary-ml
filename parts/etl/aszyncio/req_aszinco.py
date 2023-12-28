import asyncio
from random import randint
import pdb 
from time import perf_counter
import requests

MAX_POKEMON = 898

def get_pokemon() -> str:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1,MAX_POKEMON)}")
    #pdb.set_trace()
    return response.json()["name"]

async def get_pokemon_async() -> str:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1,MAX_POKEMON)}")
    #pdb.set_trace()
    return response.json()["name"]


async def main() -> None:
    
    # for _ in range(20):
    #     pokemon_name = await get_pokemon()
    #     print(pokemon_name)
    time_before = perf_counter()
    for _ in range(20):
        pokemon_name = get_pokemon()
        print(pokemon_name)
    print(f"Total time for Sync: {perf_counter() - time_before}")
    ## Total time for Sync: 7.990709944

    time_before = perf_counter()
    result = await asyncio.gather(*[get_pokemon_async() for _ in range(20)])
    print(result)
    print(f"Total time for Sync: {perf_counter() - time_before}")
    ## Total time for Sync: 5.288627230000001

if __name__ == "__main__":
    asyncio.run(main())