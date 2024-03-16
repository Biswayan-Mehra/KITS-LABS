def FIFO_replacement(pages, frames):
    hits = 0
    misses = 0
    page_frames = list()
    for page in pages:
        if page not in page_frames:
            page_frames.append(page)
            misses += 1
        else:
            hits += 1
        while len(page_frames) > frames:
            page_frames = page_frames[1:]
    return hits, misses

def LRU_replacement(pages, frames):
    hits = 0
    misses = 0
    page_frames = list()
    for page in pages:
        if page not in page_frames:
            page_frames.append(page)
            misses += 1
        else:
            page_frames.remove(page)
            page_frames.append(page)
            hits += 1
        while len(page_frames) > frames:
            page_frames = page_frames[1:]
    return hits, misses

def optimal_replacement(pages, frames):
    hits = 0
    misses = 0
    upcoming = dict((page, pages.count(page)) for page in pages)
    page_frames = list()
    for page in pages:
        upcoming[page] -= 1
        if page in page_frames:
            hits += 1
        else:
            misses += 1
            while len(page_frames) >= frames:
                page_to_remove = page_frames[0]
                for cached_page in page_frames[1:]:
                    if upcoming[cached_page] < upcoming[page_to_remove]:
                        page_to_remove = cached_page
                page_frames.remove(page_to_remove)
            page_frames.append(page)
    return hits, misses

frames = int(input("Enter number of frames: "))
pages = [int(p) for p in input("Enter pages: ").split()]

print("Running first in first out replacement algorithm, ", end = "")
hits, misses = FIFO_replacement(pages, frames)
print("resulted in", hits, "hits and", misses, "page faults")

print("Running least recently used replacement algorithm, ", end = "")
hits, misses = LRU_replacement(pages, frames)
print("resulted in", hits, "hits and", misses, "page faults")

print("Running optimal replacement algorithm, ", end = "")
hits, misses = optimal_replacement(pages, frames)
print("resulted in", hits, "hits and", misses, "page faults")

