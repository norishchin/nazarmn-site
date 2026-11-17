// Town pages. Market numbers must come from a named, linked, dated source.
// Source: Minneapolis Area REALTORS, 2024 Annual Housing Market Report (published January 2025), NorthstarMLS data.
// TODO: refresh with the 2025 annual report when it is posted at mplsrealtor.com.
export const SOURCE = {
  name: "Minneapolis Area REALTORS, 2024 Annual Housing Market Report",
  url: "https://mplsrealtor.com/wp-content/uploads/2025/01/2024-Annual-Housing-Report.pdf",
  period: "full year 2024",
  published: "January 2025",
};

export const METRO = { sales: 45145, median: 380000, days: 45, pctOrig: 98.7 };

export interface Town {
  slug: string;
  name: string;
  county: string;
  sales: number;
  salesChange: string; // vs 2023
  newConstruction: number; // % of sales
  townhouseCondo: number; // % of sales
  days: number; // cumulative days on market
  pctOrig: number; // % of original list price received
  medians: [number, number, number, number, number]; // 2020..2024
  intro: string;
  homes: string;
  nearby: string[];
}

export const TOWNS: Town[] = [
  {
    slug: "chaska", name: "Chaska", county: "Carver County",
    sales: 423, salesChange: "+14.3%", newConstruction: 24.3, townhouseCondo: 25.5, days: 41, pctOrig: 98.6,
    medians: [350000, 375000, 419990, 415000, 465500],
    intro: "Chaska is the Carver County seat, on the Minnesota River southwest of Minneapolis.",
    homes: "Nearly a quarter of Chaska's 2024 sales were new construction, which is high for the west metro. That means resale sellers often compete with builders, and buyers can weigh a new build against an existing home.",
    nearby: ["chanhassen", "eden-prairie"],
  },
  {
    slug: "chanhassen", name: "Chanhassen", county: "Carver County",
    sales: 338, salesChange: "-6.4%", newConstruction: 3.6, townhouseCondo: 30.8, days: 35, pctOrig: 99.1,
    medians: [410000, 504111, 525000, 510000, 538500],
    intro: "Chanhassen sits between Chaska and Eden Prairie, with lakes on its west side and Highway 5 and 212 running through it.",
    homes: "Chanhassen had the highest median price of the three towns on this site in 2024, and homes sold the fastest: 35 days on average, at 99.1% of the original list price. Very little of it was new construction, so most buyers here are choosing between existing homes.",
    nearby: ["chaska", "eden-prairie"],
  },
  {
    slug: "eden-prairie", name: "Eden Prairie", county: "Hennepin County",
    sales: 754, salesChange: "+3.0%", newConstruction: 2.1, townhouseCondo: 42.0, days: 43, pctOrig: 98.7,
    medians: [380000, 425000, 452500, 462000, 465000],
    intro: "Eden Prairie is in southwest Hennepin County. My office, RE/MAX Results, is on West 78th Street here.",
    homes: "Eden Prairie is the busiest of the three markets, with 754 sales in 2024. Townhouses and condos made up 42% of them, so it is one of the better places in the west metro to find a first home or a smaller place after selling a bigger one.",
    nearby: ["chanhassen", "chaska"],
  },
];

export const money = (n: number) => "$" + n.toLocaleString("en-US");
