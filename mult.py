import asyncio
import time

# ==========================================
# 1. RESOURCE CONFIGURATION
# ==========================================
# TODO: Set OVEN_CAPACITY to 2
PAN_CAPACITY  = 2
OVEN_CAPACITY = 1 

# TODO: Initialize oven_semaphore using OVEN_CAPACITY
pan_semaphore  = asyncio.Semaphore(PAN_CAPACITY)
oven_semaphore = None 

start_time = time.time()

# ==========================================
# 2. LOGGING UTILITY
# ==========================================
async def log_event(cust_id, item, msg):
    """Prints a timestamped log for a specific customer's item."""
    elapsed = time.time() - start_time
    print(f"[{elapsed:6.2f}s] [Cust {cust_id:02d}] {item:10} | {msg}")

# ==========================================
# 3. COOKING TASKS
# ==========================================
async def cook_steak(cust_id):
    await log_event(cust_id, "STEAK", "Waiting for a pan...")
    async with pan_semaphore:
        await log_event(cust_id, "STEAK", "Got a pan! Searing...")
        await asyncio.sleep(2)
    await log_event(cust_id, "STEAK", "Finished. Pan is free.")

async def bake_cake(cust_id):
    # TODO: Log 'Waiting for oven...'
    # TODO: Use 'async with' to acquire the oven_semaphore
    # TODO: Log 'Baking...', sleep for 5s, then log 'Oven is free.'
    pass

# ==========================================
# 4. RESTAURANT SIM
# ==========================================
async def serve_customer(cust_id):
    """A customer's meal consists of a steak and a cake cooked concurrently."""
    # TODO: Use asyncio.gather() to cook_steak and bake_cake at the same time
    await asyncio.gather(
        cook_steak(cust_id),
    )
    
    await log_event(cust_id, "MEAL", "****** FULL MEAL SERVED! ******")

async def main():
    print(f"--- OPENING KITCHEN (Pans: {PAN_CAPACITY}, Ovens: {OVEN_CAPACITY}) ---")
    
    # TODO: Use asyncio.gather() to run all customers concurrently
    await asyncio.gather(
        serve_customer(1),
        serve_customer(2),
    )
    
    print("--- DOORS CLOSED ---")

if __name__ == "__main__":
    asyncio.run(main())