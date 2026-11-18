// Town pages. Market numbers must come from a named, linked, dated source.
// Source: Minneapolis Area REALTORS, 2025 Annual Housing Market Report (current as of January 8, 2026), NorthstarMLS data.
// Medians are 2021 to 2025 as printed in that report. Update every January when the next annual report is out.
export const YEAR = 2025;
export const YEARS = [2021, 2022, 2023, 2024, 2025];
export const UPDATED = "November 2026";
export const SOURCE = {
  name: "Minneapolis Area REALTORS, 2025 Annual Housing Market Report",
  url: "https://maar.stats.10kresearch.com/docs/ann/x/report",
  period: "full year 2025",
  published: "January 2026",
};

// 16-county Twin Cities region, 2025.
export const METRO = { sales: 46254, median: 390000, days: 49, pctOrig: 98.7 };

export interface Town {
  slug: string;
  name: string;
  county: string;
  sales: number;
  salesChange: string; // vs the year before
  newConstruction: number; // % of sales
  townhouseCondo: number; // % of sales
  days: number; // cumulative days on market
  pctOrig: number; // % of original list price received
  medians: [number, number, number, number, number]; // YEARS
  intro: string;
  homes: string;
  nearby: string[];
  pros?: string[]; // about homes and the market only, never about the people who live there (fair housing)
  cons?: string[];
}

export const TOWNS: Town[] = [
  {
    slug: "chaska", name: "Chaska", county: "Carver County",
    sales: 447, salesChange: "+5.4%", newConstruction: 20.8, townhouseCondo: 26.8, days: 54, pctOrig: 98.3,
    medians: [375000, 419990, 415000, 465750, 485000],
    intro: "Chaska is the Carver County seat, on the Minnesota River southwest of Minneapolis.",
    homes: "About one in five Chaska sales in 2025 was new construction, among the highest shares in the west metro. Resale sellers compete with builders here, and homes took 54 days on average to sell, slower than the Twin Cities as a whole. Buyers often have time to compare a new build with an existing home.",
    nearby: ["chanhassen", "victoria", "shakopee"],
    pros: ["Plenty of new construction to choose from (20.8% of 2025 sales)", "Median price well below Chanhassen and Victoria next door", "Sales grew 5.4% in 2025"],
    cons: ["Resale sellers compete with builders", "54 days on market on average, the second slowest of the 11 towns here"],
  },
  {
    slug: "chanhassen", name: "Chanhassen", county: "Carver County",
    sales: 344, salesChange: "+1.8%", newConstruction: 2.9, townhouseCondo: 39.2, days: 48, pctOrig: 98.1,
    medians: [504111, 525000, 510000, 538500, 550500],
    intro: "Chanhassen sits between Chaska and Eden Prairie, with lakes on its west side and Highway 5 and 212 running through it.",
    homes: "Chanhassen had the second-highest median price of the towns on this site in 2025, after Victoria, at $550,500. Very little of it was new construction, so most buyers are choosing between existing homes, and townhouses and condos made up almost 40% of sales.",
    nearby: ["chaska", "victoria", "eden-prairie"],
    pros: ["Prices held up: median up about 2% in 2025", "Almost 40% townhouses and condos, so there are options below the median"],
    cons: ["Second-highest median of the 11 towns ($550,500)", "Very little new construction (2.9%)", "Sellers got 98.1% of list price, tied for the lowest here, so pricing matters"],
  },
  {
    slug: "eden-prairie", name: "Eden Prairie", county: "Hennepin County",
    sales: 753, salesChange: "-0.3%", newConstruction: 4.0, townhouseCondo: 41.6, days: 47, pctOrig: 98.6,
    medians: [425000, 452500, 462000, 465000, 475000],
    intro: "Eden Prairie is in southwest Hennepin County. My office, RE/MAX Results, is on West 78th Street here.",
    homes: "Eden Prairie had 753 sales in 2025, about the same as the year before. Townhouses and condos made up 41.6% of them, one of the highest shares in the west metro, which makes it a good place to look for a first home or a smaller place after selling a bigger one.",
    nearby: ["chanhassen", "hopkins", "chaska"],
    pros: ["Large market with 753 sales, so lots of choice and good comps", "41.6% townhouses and condos"],
    cons: ["Little new construction (4.0%)", "Median up only about 2% in 2025"],
  },
  {
    slug: "victoria", name: "Victoria", county: "Carver County",
    sales: 277, salesChange: "+25.3%", newConstruction: 39.0, townhouseCondo: 27.8, days: 48, pctOrig: 98.8,
    medians: [527500, 619950, 600000, 610000, 650000],
    intro: "Victoria is in Carver County, just west of Chanhassen.",
    homes: "Victoria had the highest median price of any town on this site in 2025, $650,000, and the most new construction: 39% of sales. Sales jumped 25.3% from 2024. Resale sellers here are pricing against builders, who can offer incentives a homeowner can't.",
    nearby: ["chanhassen", "chaska"],
    pros: ["Most new construction of the 11 towns (39.0% of sales)", "Busy year: sales up 25.3%"],
    cons: ["Highest median here ($650,000)", "Smaller market: 277 sales", "Resale sellers price against builders' incentives"],
  },
  {
    slug: "hopkins", name: "Hopkins", county: "Hennepin County",
    sales: 173, salesChange: "-7.0%", newConstruction: 0.0, townhouseCondo: 37.6, days: 44, pctOrig: 98.3,
    medians: [287000, 315000, 325000, 373000, 365000],
    intro: "Hopkins is a small city in Hennepin County, next to Minnetonka, St. Louis Park and Edina, with a walkable Mainstreet downtown.",
    homes: "Hopkins is the smallest market on this site, with 173 sales in 2025, and the least expensive: a $365,000 median. There was no new construction in the 2025 numbers, and townhouses and condos made up 37.6% of sales. The median dipped about 2% after a big jump in 2024, so recent comps matter more than older ones.",
    nearby: ["eden-prairie", "plymouth"],
    pros: ["Lowest median price of the 11 towns ($365,000)", "Homes sold in 44 days on average, faster than the metro"],
    cons: ["Smallest market: only 173 sales in 2025", "No new construction in the 2025 numbers", "Median moved a lot in two years, so price on recent sales"],
  },
  {
    slug: "savage", name: "Savage", county: "Scott County",
    sales: 378, salesChange: "+3.6%", newConstruction: 8.2, townhouseCondo: 33.9, days: 44, pctOrig: 99.1,
    medians: [390000, 421000, 415000, 425000, 431250],
    intro: "Savage is in Scott County, south of the Minnesota River across from Bloomington.",
    homes: "Savage was steady again in 2025: sales up 3.6% and the median up about 1.5%. Sellers got 99.1% of their original list price, the second highest of the 11 towns, and homes sold in 44 days on average. About a third of sales were townhouses or condos.",
    nearby: ["prior-lake", "burnsville", "shakopee"],
    pros: ["Sellers got 99.1% of list price, second highest here", "Homes sold in 44 days on average"],
    cons: ["Prices rose only about 1.5% in 2025", "Well-priced homes go quickly, so buyers need to be ready"],
  },
  {
    slug: "shakopee", name: "Shakopee", county: "Scott County",
    sales: 688, salesChange: "+5.0%", newConstruction: 27.9, townhouseCondo: 34.6, days: 45, pctOrig: 98.5,
    medians: [340257, 400000, 385000, 400000, 413433],
    intro: "Shakopee is the Scott County seat, on the south bank of the Minnesota River.",
    homes: "Shakopee sales grew 5% in 2025, and 27.9% of them were new construction, second only to Victoria among the towns on this site. The median moved past $400,000 to about $413,000 after holding near $400,000 for three years.",
    nearby: ["savage", "prior-lake", "chaska"],
    pros: ["Median about $413,000, among the lower prices here", "Sales up 5.0% in 2025", "Lots of new construction (27.9% of sales)"],
    cons: ["Resale sellers compete with builders", "Prices moved slowly from 2022 to 2024"],
  },
  {
    slug: "burnsville", name: "Burnsville", county: "Dakota County",
    sales: 643, salesChange: "-5.0%", newConstruction: 0.2, townhouseCondo: 43.1, days: 46, pctOrig: 98.7,
    medians: [335000, 355000, 356000, 375000, 378750],
    intro: "Burnsville is in Dakota County, south of the Minnesota River where I-35W and I-35E meet.",
    homes: "Burnsville's 2025 median of $378,750 sat just under the Twin Cities region median of $390,000. Townhouses and condos were 43.1% of sales, the highest share of the 11 towns, and almost nothing was new construction, so buyers are choosing among existing homes and the condition of each one matters.",
    nearby: ["savage", "prior-lake"],
    pros: ["Median $378,750, just under the Twin Cities region", "Most townhouses and condos of the 11 towns (43.1%)"],
    cons: ["Almost no new construction (0.2%)", "Sales down 5.0% in 2025"],
  },
  {
    slug: "prior-lake", name: "Prior Lake", county: "Scott County",
    sales: 408, salesChange: "-8.1%", newConstruction: 5.6, townhouseCondo: 29.7, days: 59, pctOrig: 98.1,
    medians: [450000, 494900, 475000, 495000, 483750],
    intro: "Prior Lake is in Scott County, built around Upper and Lower Prior Lake.",
    homes: "Prior Lake homes took the longest to sell of any town on this site in 2025, 59 days on average, and the median slipped about 2% to $483,750. Sellers got 98.1% of their original list price. That's where pricing right at launch pays off most, and where buyers usually have more room to negotiate.",
    nearby: ["savage", "shakopee"],
    pros: ["Buyers have the most time and room to negotiate here", "Median dipped about 2% in 2025"],
    cons: ["Slowest market here: 59 days on average", "Sales down 8.1% in 2025", "Overpriced listings tend to sit"],
  },
  {
    slug: "plymouth", name: "Plymouth", county: "Hennepin County",
    sales: 1074, salesChange: "-1.8%", newConstruction: 4.7, townhouseCondo: 36.4, days: 46, pctOrig: 98.9,
    medians: [440000, 466500, 483750, 500500, 497175],
    intro: "Plymouth is in Hennepin County, northwest of Minneapolis, and wraps around most of Medicine Lake.",
    homes: "Plymouth had 1,074 sales in 2025, second only to Maple Grove among the towns on this site. The median held just under $500,000. With that many sales, there are plenty of recent comps, so pricing can be precise down to the neighborhood.",
    nearby: ["maple-grove", "hopkins"],
    pros: ["Big market: 1,074 sales, so lots of choice and solid comps", "Sellers got 98.9% of list price"],
    cons: ["Median near $500,000", "Prices flat in 2025"],
  },
  {
    slug: "maple-grove", name: "Maple Grove", county: "Hennepin County",
    sales: 1188, salesChange: "+15.2%", newConstruction: 14.4, townhouseCondo: 36.4, days: 38, pctOrig: 99.2,
    medians: [371000, 400000, 389300, 404000, 432000],
    intro: "Maple Grove is in northwest Hennepin County, along I-94 and Highway 610.",
    homes: "Maple Grove was the busiest and fastest market on this site in 2025: 1,188 sales, up 15.2%, with homes selling in 38 days on average and sellers getting 99.2% of their original list price. The median rose about 7% to $432,000.",
    nearby: ["plymouth"],
    pros: ["Busiest market here: 1,188 sales", "Fastest sales: 38 days on average", "Sellers got 99.2% of list price, the highest here"],
    cons: ["Median up about 7% in 2025, so prices are climbing", "Good homes go fast, so buyers need to be ready"],
  },
];

export const money = (n: number) => "$" + n.toLocaleString("en-US");
