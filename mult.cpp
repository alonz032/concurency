import asyncio
import time

# --- GLOBAL RESOURCES ---
stove_lock = asyncio.Lock()
# TODO: Declare an asyncio.Lock() for the airfryer_lock

start_time = time.time()

# --- LOGGING ---
async def log_event(task, msg):
    elapsed = time.time() - start_time
    print(f"[{elapsed:6.2f}s] [{task}] | {msg}")

# --- INDEPENDENT TASKS ---

async def make_tea():
    await log_event("TEA", "Starting steep...")
    await asyncio.sleep(2)
    await log_event("TEA", "Finished.")

# TODO: Implement cut_avocado()
# Should log "Starting", sleep for 1s, and log "Finished".


# --- STOVE TASKS (Group 1: Pre-filled Example) ---

async def make_eggs():
    await log_event("EGGS", "Waiting for Stove...")
    async with stove_lock:
        await log_event("EGGS", "Got Stove. Cooking...")
        await asyncio.sleep(3)
    await log_event("EGGS", "Finished. Released Stove.")

async def make_ham():
    await log_event("HAM", "Waiting for Stove...")
    async with stove_lock:
        await log_event("HAM", "Got Stove. Cooking...")
        await asyncio.sleep(3)
    await log_event("HAM", "Finished. Released Stove.")

# --- AIRFRYER TASKS (Group 2) ---

# TODO: Implement make_hashbrowns() and make_waffles()
# Both should:
# 1. Log "Waiting for Airfryer..."
# 2. Use "async with" with the airfryer_lock (once declared)
# 3. Log "Got Airfryer. Cooking..."
# 4. Sleep for 4s using asyncio.sleep()
# 5. Log "Finished. Released Airfryer."


# --- THE MAIN KITCHEN ---

async def main():
    print("--- STARTING ASYNC KITCHEN ---")
    
    # --- TODO: INITIALIZE AND RUN ALL TASKS ---
    # Use asyncio.gather() to run all tasks concurrently:
    # tea, eggs, ham, hashbrowns, waffles, and avocado.
    
    await asyncio.gather(
        make_tea(),
        make_eggs(),
        make_ham(),
        # Add the remaining tasks here...
    )

    print("--- ALL TASKS COMPLETE ---")

if __name__ == "__main__":
    asyncio.run(main())