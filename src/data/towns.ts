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
    nearby: ["chanhassen", "victoria", "shakopee"],
  },
  {
    slug: "chanhassen", name: "Chanhassen", county: "Carver County",
    sales: 338, salesChange: "-6.4%", newConstruction: 3.6, townhouseCondo: 30.8, days: 35, pctOrig: 99.1,
    medians: [410000, 504111, 525000, 510000, 538500],
    intro: "Chanhassen sits between Chaska and Eden Prairie, with lakes on its west side and Highway 5 and 212 running through it.",
    homes: "Chanhassen had the second-highest median price of the towns on this site in 2024, after Victoria, and homes sold quickly: 35 days on average, at 99.1% of the original list price. Very little of it was new construction, so most buyers here are choosing between existing homes.",
    nearby: ["chaska", "victoria", "eden-prairie"],
  },
  {
    slug: "eden-prairie", name: "Eden Prairie", county: "Hennepin County",
    sales: 754, salesChange: "+3.0%", newConstruction: 2.1, townhouseCondo: 42.0, days: 43, pctOrig: 98.7,
    medians: [380000, 425000, 452500, 462000, 465000],
    intro: "Eden Prairie is in southwest Hennepin County. My office, RE/MAX Results, is on West 78th Street here.",
    homes: "Eden Prairie had 754 sales in 2024. Townhouses and condos made up 42% of them, so it is one of the better places in the west metro to find a first home or a smaller place after selling a bigger one.",
    nearby: ["chanhassen", "hopkins", "chaska"],
  },
  {
    slug: "victoria", name: "Victoria", county: "Carver County",
    sales: 219, salesChange: "-9.9%", newConstruction: 42.9, townhouseCondo: 29.2, days: 52, pctOrig: 98.7,
    medians: [481280, 527500, 619950, 600000, 600400],
    intro: "Victoria is in Carver County, just west of Chanhassen.",
    homes: "Victoria had the highest median price of any town on this site in 2024, and the highest share of new construction: 42.9% of sales. Resale sellers here are pricing against builders, who can offer incentives a homeowner can't. Homes also took longer to sell than in most nearby towns, at 52 days.",
    nearby: ["chanhassen", "chaska"],
  },
  {
    slug: "hopkins", name: "Hopkins", county: "Hennepin County",
    sales: 185, salesChange: "-1.6%", newConstruction: 0.5, townhouseCondo: 46.5, days: 33, pctOrig: 98.3,
    medians: [282500, 287000, 315000, 325000, 371000],
    intro: "Hopkins is a small city in Hennepin County, next to Minnetonka, St. Louis Park and Edina, with a walkable Mainstreet downtown.",
    homes: "Hopkins is the smallest market on this site, with 185 sales in 2024, and the fastest: 33 days on average. Townhouses and condos made up 46.5% of sales, the highest share of any town here. The median jumped from $325,000 in 2023 to $371,000 in 2024, so recent sales matter more than older ones when pricing.",
    nearby: ["eden-prairie", "plymouth"],
  },
  {
    slug: "savage", name: "Savage", county: "Scott County",
    sales: 365, salesChange: "0.0%", newConstruction: 7.1, townhouseCondo: 31.0, days: 43, pctOrig: 98.8,
    medians: [349900, 390000, 421000, 415000, 425000],
    intro: "Savage is in Scott County, south of the Minnesota River across from Bloomington.",
    homes: "Savage was steady in 2024: the same number of sales as 2023 and a median up about 2%. About a third of sales were townhouses or condos. At 43 days and 98.8% of list price, a well-priced home here sells close to asking without a bidding war.",
    nearby: ["prior-lake", "burnsville", "shakopee"],
  },
  {
    slug: "shakopee", name: "Shakopee", county: "Scott County",
    sales: 653, salesChange: "+8.8%", newConstruction: 28.5, townhouseCondo: 33.8, days: 40, pctOrig: 98.5,
    medians: [305000, 340257, 400000, 385000, 400000],
    intro: "Shakopee is the Scott County seat, on the south bank of the Minnesota River.",
    homes: "Shakopee sales grew 8.8% in 2024, and 28.5% of them were new construction, second only to Victoria among the towns on this site. The median of $400,000 is right at the 2022 level, so prices here have held flat for two years while sales picked up.",
    nearby: ["savage", "prior-lake", "chaska"],
  },
  {
    slug: "burnsville", name: "Burnsville", county: "Dakota County",
    sales: 677, salesChange: "-4.2%", newConstruction: 2.1, townhouseCondo: 41.8, days: 36, pctOrig: 98.9,
    medians: [298799, 335000, 355000, 356000, 375000],
    intro: "Burnsville is in Dakota County, south of the Minnesota River where I-35W and I-35E meet.",
    homes: "Burnsville's 2024 median of $375,000 sat just under the Twin Cities region median, and homes sold in 36 days on average. Townhouses and condos were 41.8% of sales, and almost nothing was new construction, so buyers are choosing among existing homes and the condition of each one matters.",
    nearby: ["savage", "prior-lake"],
  },
  {
    slug: "prior-lake", name: "Prior Lake", county: "Scott County",
    sales: 443, salesChange: "-3.9%", newConstruction: 10.4, townhouseCondo: 27.3, days: 59, pctOrig: 97.4,
    medians: [400000, 450000, 494900, 475000, 495000],
    intro: "Prior Lake is in Scott County, built around Upper and Lower Prior Lake.",
    homes: "Prior Lake homes took the longest to sell of any town on this site in 2024, 59 days on average, and sellers got the lowest share of their original price, 97.4%. That's where pricing right at launch pays off most. Buyers here usually have more room to negotiate than in the faster towns.",
    nearby: ["savage", "shakopee"],
  },
  {
    slug: "plymouth", name: "Plymouth", county: "Hennepin County",
    sales: 1094, salesChange: "+3.8%", newConstruction: 7.8, townhouseCondo: 36.1, days: 44, pctOrig: 98.8,
    medians: [392000, 440000, 466500, 483750, 500500],
    intro: "Plymouth is in Hennepin County, northwest of Minneapolis, and wraps around most of Medicine Lake.",
    homes: "Plymouth was the busiest market on this site in 2024, with 1,094 sales, and the median crossed $500,000 for the first time in this five-year span. With that many sales, there are plenty of recent comps, so pricing can be precise down to the neighborhood.",
    nearby: ["maple-grove", "hopkins"],
  },
  {
    slug: "maple-grove", name: "Maple Grove", county: "Hennepin County",
    sales: 1030, salesChange: "+5.7%", newConstruction: 7.7, townhouseCondo: 40.4, days: 39, pctOrig: 99.1,
    medians: [337400, 371000, 400000, 389600, 403700],
    intro: "Maple Grove is in northwest Hennepin County, along I-94 and Highway 610.",
    homes: "Maple Grove had 1,030 sales in 2024, second only to Plymouth among the towns on this site, and sellers got 99.1% of their original list price, tied with Chanhassen for the highest. Townhouses and condos were 40.4% of sales.",
    nearby: ["plymouth"],
  },
];

export const money = (n: number) => "$" + n.toLocaleString("en-US");
