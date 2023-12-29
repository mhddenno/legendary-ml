import asyncio
from random import randint
import pdb 
from time import perf_counter
import requests
from typing import Any, Dict


MAX_POKEMON = 898

def get_pokemon() -> str:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1,MAX_POKEMON)}")
    #pdb.set_trace()
    return response.json()["name"]

def get_pokemon_sync_func() -> Dict[str, Any]:
    reasponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1,MAX_POKEMON)}")
    return reasponse.json()

async def get_pokemon_async() -> str:
    response = await asyncio.to_thread(get_pokemon_sync_func) 
    #pdb.set_trace()
    return response["name"]


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
    ## Total time for Sync: 0.8832137910000002

if __name__ == "__main__":
    asyncio.run(main())