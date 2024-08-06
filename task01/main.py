import heapq

def main():
    cables = [4, 2, 1, 6, 12]
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на їх з'єднання
        cost = first + second
        total_cost += cost

        # Вставляємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    print("Мінімальні витрати на з'єднання кабелів:", total_cost)


if __name__ == "__main__":
    main()


